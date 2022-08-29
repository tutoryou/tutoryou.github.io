# COMP1521
## 简介
- 课程名称：COMP1521 Computer Systems Fundamentals

- 前置课(prerequisite): COMP1511 或者 DPST1091 或者 COMP1911 或者 COMP1917

- 每周上课时长(contact hour)：2个2小时lecture + 1个1小时tutorial + 1个2小时lab

- 作业布置：Assignment 1 (15%）+ Assignment 2 (15%）+ Weekly Tests (10%) + Labs (15%) + Final (45%)

- 讲师(Lecturer)：Dr Andrew Taylor

- 难度：1/5, 3.5/5 (Final)

## 总体评价


这门课是 Computer Science, Software/Electrical/Bioinformatic Engineerin的一年级必修课之一，觉得 1151 比较有趣不痛苦的同学可能会觉得 1521 更加有趣但是略带一点点痛苦。有趣的地方在于学生们们能够了解当程序运行时，系统内部正在发生着些什么；存储怎么调配，整数，浮点小数，字符和他们的 array 怎么被表示以及储存在记忆体中。

学生们认为这门课的内容比COMP1511还要再简单上一些，但是 assignments last stage 的难度却比 1511 难上不少。Though they were meant to be challenging；1511的难是略加思考和 carefully coding 就可以解决的，但是1521 的难在于它需要学生去自己搜索课外的知识然后 carefully experiment 才有可能做出来。换句话来说就是，它是有些许"超纲"了的。

## 教师评价
Andrew 是一个 demanding 的老师。他上课的风格是不太爱 dry-teach？(这里dry-teach是指把每个 function 每行 code 都先细细得讲一遍)。他喜欢每节课都拿出好多个写好的programs 给学生们们看然后跑，再告诉学生们们这个 program 能干什么。如果有用到不常见的function 他再解释两句。基本上他需要学生们们下课之后再把他的代码捋一遍，把每行代码的的意思都搞明白，因为他觉得这样才是学到最多的方法 lol。

他的个别 challenging labs 是 almost impossible，连 solution 都是 fake 出来的。

## 授课环节评价
学生们觉得最有趣的是数字在不同进制里的表示法。MATH2301 里面也有讲过，但侧重点完全不同；MATH2301 讲的非常理论（学生们不喜欢），表示算法比 COMP1521 严谨。

其实课件 8-12 里面的内容都是非常浅地过一遍。比如课件 8 粗略介绍了一遍操作系统到底是什么 + virtual memory/physical memory，听完对课件 8 内容感兴趣的同学 Andrew 推荐去上 COMP3231/3891（undergrad）, COMP9201/9283（postgrad）。课件 9 则交给学生们们 emoji 和 一些复杂的外语文字怎么用 unicode 表示。

作业
- Weekly Tests：从第三周开始，每周都有一个，难度偏简单，每次3道题。测的内容就是上一周课上教的 （比如第六周的 test 就是考察第五周的课教的）。如果你在给定的一个小时之内没有把题目都做出来，那你就要反思你自己了。要么是没 catch up，要么是你没学懂。一般本周的 test 都会在 本周的星期三出来，下个星期三截止（比如第六周 test 会在第六周星期三出，第七周星期三 due ）。

- Assignment 1：用 C 语言写一个模拟 MIPS 的程序，Andrew 很照顾学生们们，除了implementation，starter code 里面什么都帮学生们们做好了。而且学生们们要模拟的都只是几个非常简单的 MIPS operations。

- Assignment 2：用 C 语言写一个 file archive，工程量比 ass1 大上不少，一共5个subsets，越到后面越难。最后一个 subset 需要学生们们自己查资料然后用 posix_spawn() 或者 posix_spawnp 加上 pipe，在程序之外开一个新的 process 然后用 Linux 自带的 xz 程序压缩或者解压缩文档。

- Final：一共11道编程题，没有理论题，题号越大难度越大。基本上没什么人能写出最后一道题，要么太难，要么没有时间。考前有给学生们们 sample paper。

## 联系我

最后。如果同学们在本门课程的任何环节中遇到问题，欢迎随时与我联系！

我可以在任何环节提供包括授课在内的任何形式的辅导。

欢迎加我微信联系： Tutor_0914

![图片](../image/wechat.jpg)