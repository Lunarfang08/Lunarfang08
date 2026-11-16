import os, json, urllib.request, urllib.parse, subprocess, tempfile, re
from pathlib import Path
from datetime import datetime, timezone

USER = 'Lunarfang08'
TOKEN = os.environ['GITHUB_TOKEN']
ROOT = Path(__file__).resolve().parents[1]

def api(path):
    req = urllib.request.Request('https://api.github.com'+path, headers={'Authorization':f'Bearer {TOKEN}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
    with urllib.request.urlopen(req, timeout=60) as r: return json.load(r)

def pages(path):
    for n in range(1,10000):
        batch=api(path+('&' if '?' in path else '?')+f'per_page=100&page={n}')
        yield from batch
        if len(batch)<100: return
    raise RuntimeError('Pagination limit reached')

def search_count(query):
    return api('/search/issues?q='+urllib.parse.quote(query))['total_count']

profile=api('/users/'+USER)
repos=list(pages(f'/users/{USER}/repos?type=owner'))
owned=[r for r in repos if not r['fork']]
# Public owned non-fork repositories, default-branch history only. Match author emails.
emails={'arsaladnan07@gmail.com',f'{USER.lower()}@users.noreply.github.com',f"{profile['id']}+{USER.lower()}@users.noreply.github.com"}
if profile.get('email'): emails.add(profile['email'].lower())
emails.update(e.strip().lower() for e in os.getenv('EXTRA_AUTHOR_EMAILS','').split(',') if e.strip())
seen=set(); added=deleted=commits=0
with tempfile.TemporaryDirectory() as tmp:
    for i,r in enumerate(owned):
        if not r['size']: continue
        dest=Path(tmp)/str(i)
        subprocess.run(['git','clone','--quiet','--bare','--single-branch','--branch',r['default_branch'],r['clone_url'],str(dest)],check=True)
        log=subprocess.check_output(['git','--git-dir',str(dest),'log','--no-merges','--format=%x1e%H%x09%ae','--numstat','--no-renames'],text=True,errors='replace')
        for entry in log.split('\x1e')[1:]:
            lines=entry.strip().splitlines()
            if not lines: continue
            sha,email=lines[0].split('\t',1)
            if email.lower() not in emails or sha in seen: continue
            seen.add(sha); commits+=1
            for line in lines[1:]:
                fields=line.split('\t',2)
                if len(fields)==3 and fields[0].isdigit() and fields[1].isdigit():
                    added+=int(fields[0]); deleted+=int(fields[1])
prs=search_count(f'author:{USER} is:pr is:public')
issues=search_count(f'author:{USER} is:issue is:public')
# GitHub search counts public PRs/issues; external PR repository count is not equivalent to all contributed repositories.
svg=ROOT/'assets/spider-fetch.svg'
s=svg.read_text(); s=s.replace('height="580"','height="700"').replace('900 580','900 700').replace('height="578"','height="698"')
start=s.index('<text x="34" y="509"')
end=s.index('</g>',start)
rows=[('Public repos',f'{len(repos):,}   |   Stars: {sum(r["stargazers_count"] for r in repos):,}'),('Commits',f'{commits:,}   |   Followers: {profile["followers"]:,}'),('Lines of code',f'{added-deleted:,}   ( {added:,}++  /  {deleted:,}-- )'),('Pull requests',f'{prs:,}   |   Issues: {issues:,}')]
from xml.sax.saxutils import escape
out=[]
for i,(k,v) in enumerate(rows):
    y=509+i*30
    out.append(f'<text x="34" y="{y}" fill="#ff5268">{k}:</text><text x="866" y="{y}" text-anchor="end" fill="#eaeaea">{escape(v)}</text>')
    a=34+(len(k)+2)*11.45; b=866-len(v)*11.45-12
    if b>a: out.append(f'<path d="M{a} {y-5} H{b}" stroke="#55555d" stroke-width="3" stroke-dasharray="3 7"/>')
out.append('<text x="34" y="650" fill="#888891" font-size="14">Commits / LOC: authored non-merge commits in owned public non-fork default branches.</text>')
out.append(f'<text x="34" y="674" fill="#888891" font-size="14">Updated: {datetime.now(timezone.utc):%Y-%m-%d} UTC · LOC = additions minus deletions</text>')
svg.write_text(s[:start]+'\n'.join(out)+'\n'+s[end:])
