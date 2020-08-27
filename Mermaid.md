# Markdown--Draw
Mermaid is a view packet for markdown,we can use it to do many thing.
### First -- draw a flowchat
#### Mermaid
```mermaid
graph LR
A["方形"] --> B("圆角")
B --> C{"条件"}
C -->|a=1| D["分支结果（1）"]
C -->|a=-1| E["分支结果（2）"]
F["横向流程图"]
```
---
#### flow
```flow
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st->op->cond
cond(yes)->io->e
cond(no)->sub1(right)->op
```
---
#### flow
```flow
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st(right)->op(right)->cond
cond(yes)->io(bottom)->e
cond(no)->sub1(right)->op
```
---
