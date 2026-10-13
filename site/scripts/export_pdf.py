#!/usr/bin/env python3
"""Export both checked A4 volumes from the same Markdown used by the VCI site."""
from pathlib import Path
import re,json,subprocess,hashlib,shutil
ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parent
WORK=REPO/'.build/pdf';WORK.mkdir(parents=True,exist_ok=True)
OUT=ROOT/'downloads';OUT.mkdir(exist_ok=True)
source=(REPO/'content/第一阶段复习讲义.md').read_text()
qa=(REPO/'content/补充问答.md').read_text()
chapters=re.split(r'(?m)(?=^# )',source)
main=[];answer=[]
for chunk in chapters:
 if chunk.startswith('# 13 '):answer.append(chunk);continue
 if chunk.startswith('# 14 '):
  question,solutions=chunk.split('## 14.2 参考答案',1)
  main.append(question);answer.append('# 14 自测变式：题目与逐步解答\n\n')
  qs=list(re.finditer(r'^\*\*(\d+)\. ',question,re.M));ans=list(re.finditer(r'^\*\*(\d+)\.\*\* ',solutions,re.M))
  assert len(qs)==len(ans)==16
  for i,(q,a) in enumerate(zip(qs,ans)):
   qt=question[q.start():qs[i+1].start() if i<15 else len(question)].strip()
   at=solutions[a.end():ans[i+1].start() if i<15 else len(solutions)].strip()
   answer.append(f'## 第 {i+1} 题\n\n{qt}\n\n**解析。** {at}\n\n')
 else:main.append(chunk)
qa=re.sub(r'(?m)^(## (Q\d+) .+)$',lambda m:m[1]+' {#'+m[2].lower()+'}',qa)
qa=qa.replace('# 补充问答','# 附录：已收录的补充问答',1)
maintext=''.join(main)+'\n\n'+qa
maintext=maintext.replace('第 13 章是去年真题的参考解析，初读可先跳过；第 14 章是独立练习，网页答案默认折叠，打印版答案另册。','网页版第 13 章是去年真题参考解析，本 PDF 将它和第 14 章练习答案放入独立答案册。为方便对照网站，正文保留原章号，从第 12 章跳到第 14 章。第 14 章题目仍在本册。')
maintext=re.sub(r'\(补充问答\.md#(Q\d+)\)',lambda m:'(#'+m[1].lower()+')',maintext)

def run(args):
 return subprocess.run(args,check=True,capture_output=True,text=True)
def walk(v):
 if isinstance(v,dict):
  yield v
  for x in v.values():yield from walk(x)
 elif isinstance(v,list):
  for x in v:yield from walk(x)
def plain(v):return ''.join(n.get('c','') for n in walk(v) if n.get('t')=='Str')
pre=r'''\documentclass[UTF8,a4paper,12pt,fontset=none]{ctexart}
\usepackage[left=17mm,right=17mm,top=18mm,bottom=18mm,headheight=15pt]{geometry}
\setCJKmainfont{Songti SC}[BoldFont={Songti SC Bold}]
\setCJKsansfont{Heiti SC}\setCJKmonofont{Heiti SC}
\usepackage{amsmath,amssymb,booktabs,longtable,array,calc,graphicx,xcolor,fancyhdr,hyperref,bookmark,enumitem,fvextra,needspace,float}
\floatplacement{figure}{H}
\definecolor{ink}{HTML}{194F69}
\hypersetup{colorlinks=true,linkcolor=ink,urlcolor=ink,pdftitle={第一阶段复习讲义·讲解版},pdfauthor={by-lastime；参考笔记署名 Sparkle}}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small 可视计算与交互概论}
\fancyhead[R]{\small 第一阶段复习 · 讲解版}
\fancyfoot[C]{\small\thepage}
\setcounter{secnumdepth}{-1}\setcounter{tocdepth}{2}
\ctexset{section={format=\Large\bfseries\sffamily\raggedright,beforeskip=0pt,afterskip=12pt},subsection={format=\fontsize{13pt}{18pt}\selectfont\bfseries\raggedright,beforeskip=12pt,afterskip=6pt},subsubsection={format=\normalsize\bfseries\raggedright,beforeskip=8pt,afterskip=4pt}}
\renewcommand{\normalsize}{\fontsize{11.5pt}{16.3pt}\selectfont
\setlength{\abovedisplayskip}{7pt}\setlength{\belowdisplayskip}{7pt}
\setlength{\abovedisplayshortskip}{4pt}\setlength{\belowdisplayshortskip}{4pt}}
\renewcommand{\small}{\fontsize{10pt}{13.5pt}\selectfont}
\renewcommand{\footnotesize}{\fontsize{9.5pt}{12.5pt}\selectfont}
\normalsize\raggedbottom
\setlength{\parindent}{0pt}\setlength{\parskip}{5pt}\setlength{\emergencystretch}{3em}
\setlength{\tabcolsep}{4pt}\renewcommand{\arraystretch}{1.08}
\setlist{leftmargin=1.6em,itemsep=3pt,topsep=4pt}
\providecommand{\tightlist}{\setlength{\itemsep}{2pt}\setlength{\parskip}{0pt}}
\providecommand{\pandocbounded}[1]{#1}
\RecustomVerbatimEnvironment{verbatim}{Verbatim}{fontsize=\footnotesize,breaklines=true,breakanywhere=true,frame=single,rulecolor=\color{ink!30},framesep=6pt}
\AddToHook{cmd/subsection/before}{\Needspace{6\baselineskip}}
\AddToHook{cmd/subsubsection/before}{\Needspace{5\baselineskip}}
\widowpenalty=10000\clubpenalty=10000\predisplaypenalty=10000
\begin{document}
\thispagestyle{empty}\vspace*{19mm}
{\color{ink}\Large 可视计算与交互概论}\par\vspace{10mm}
{\Huge\bfseries 第一阶段复习讲义}\par\vspace{5mm}
{\LARGE VOLUME}\par\vspace{11mm}
{\large 从 Lab 1 出发，补齐概念、原因与计算步骤}\par\vspace{7mm}
\rule{\linewidth}{0.6pt}\par\vspace{6mm}
INTRO\par\vspace{8mm}
by-lastime\par 发布版：2026 年 10 月 13 日\par
\vfill\small
依据提供的课程 PPT、Lab 1、原复习笔记和 2025 年第一次小测整理。
原复习笔记署名 Sparkle。真题解析为参考推导，未提供官方答案；自测变式与辅助示意图由本讲义补充。\par
\clearpage{\small\setlength{\parskip}{0pt}\tableofcontents}
'''
volumes=[('第一阶段复习讲义','讲解版 · 正文与练习',maintext,'适合已做过 Lab 1、尚未系统学习其他内容的读者。先解释问题和术语，再读公式与推导。原有知识点与延伸内容保留，独立练习答案另册。'),('第一阶段复习讲义-答案册','讲解版 · 真题解析与练习答案',''.join(answer),'建议先独立完成原卷和正文中的自测，再查看本册。保留网站第 13、14 章编号，便于回到对应概念章节复习。')]
manifest={}
for name,vol,md,intro in volumes:
 draft=WORK/(name+'.md');draft.write_text(md)
 ast=json.loads(run(['pandoc',str(draft),'-f','markdown+tex_math_dollars','-t','json']).stdout)
 for n in walk(ast):
  if n.get('t')=='Image':
   n['c'][0][2].append(['width','100%'])
   n['c'][2][0]=str(REPO/'content'/n['c'][2][0])
  if n.get('t')=='Table':
   count=len(n['c'][2]);head=plain(n['c'][3])
   widths=([.27,.73] if count==2 else [.23,.34,.43] if count==3 else [.30,.09,.22,.39] if count==4 else [1/count]*count)
   if head.startswith('符号或步骤'):widths=[.26,.74]
   if head.startswith('来源'):widths=[.43,.57]
   if head.startswith('当前绘制点'):widths=[.27,.14,.33,.26]
   if head.startswith('材料'):widths=[.35,.65]
   if head.startswith('类型名称'):widths=[.1,.24,.3,.36]
   for col,w in zip(n['c'][2],widths):col[1]={'t':'ColWidth','c':w}
 astpath=WORK/(name+'.json');astpath.write_text(json.dumps(ast,ensure_ascii=False))
 body=run(['pandoc',str(astpath),'-f','json','-t','latex','--syntax-highlighting=none','--wrap=none']).stdout
 body=body.replace(r'\def\LTcaptype{none}','')
 body=body.replace('→',r'\(\to\)').replace('−','-')
 body=body.replace(r'\section{',r'\clearpage'+'\n'+r'\section{')
 body=body.replace(r'\begin{longtable}',r'\Needspace{8\baselineskip}\begingroup\small'+'\n'+r'\begin{longtable}').replace(r'\end{longtable}',r'\end{longtable}\endgroup')
 body=re.sub(r'(\\begin\{verbatim\}.*?\\end\{verbatim\})',lambda m:r'\par\smallskip\noindent\begin{minipage}{\linewidth}'+'\n'+m[1]+'\n'+r'\end{minipage}\par\smallskip',body,flags=re.S)
 for heading in ['四类材料分别怎样使用','真题告诉我们要练什么','色域、色深、分辨率与 HDR 分别在问什么','15.1 考前最后检查','6.4 一次完整手算']:
  for command in ['subsection','subsubsection']:
   key='\\'+command+'{'+heading+'}'
   body=body.replace(key,(r'\Needspace{14\baselineskip}' if heading.startswith('6.4 ') else r'\Needspace{22\baselineskip}')+key)

 body=body.replace(r'\texttt{ppt资料/',r'{\small ppt资料/').replace(r'\texttt{往年题/',r'{\small 往年题/')
 tex=WORK/(name+'.tex');tex.write_text(pre.replace('VOLUME',vol).replace('INTRO',intro)+body+'\n\\end{document}\n')
 for i in range(3):
  result=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(WORK),str(tex)],cwd=ROOT,text=True,capture_output=True)
  (WORK/(name+f'-compile-{i}.txt')).write_text(result.stdout+result.stderr)
  if result.returncode:raise RuntimeError(result.stdout[-6000:])
 shutil.copy2(WORK/(name+'.pdf'),OUT/(name+'.pdf'))

 manifest[name]={'path':'downloads/'+name+'.pdf','math':sum(1 for n in walk(ast) if n.get('t')=='Math')}
manifest['sourceSha256']=hashlib.sha256(source.encode()).hexdigest();manifest['qaSha256']=hashlib.sha256(qa.encode()).hexdigest()
(WORK/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps(manifest,ensure_ascii=False,indent=2))
