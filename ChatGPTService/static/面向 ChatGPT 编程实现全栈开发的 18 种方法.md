![img](https://geekr.gstatics.cn/wp-content/uploads/2023/02/programing-with-chatgpt.png)

# 面向 ChatGPT 编程实现全栈开发的 18 种方法

在《[编程新手如何通过ChatGPT一天完成一个MVP产品](https://geekr.dev/posts/chatgpt-start)》这篇教程中，学院君已经给大家演示过面向 ChatGPT 编程的一些基本套路，今天这篇教程是一个更系统的介绍，希望对你提高日常开发效率、成为10倍生产力程序员有所帮助。

> 如果你还没有 ChatGPT 账号，请参考这篇教程获取：[ChatGPT 终极指南](https://geekr.dev/posts/chatgpt-ultimate-guide)。

## 0、搭建框架

首先，ChatGPT 可以帮我们开启想要编写的任何新内容的骨架结构，从而提升日常编码效率。[GitHub Copilot](https://github.com/features/copilot) 在这方面也做得很好。这里我们以远程下载图片为例进行演示。

在 VSCode 中，可以基于 [ChatGPT 插件](https://marketplace.visualstudio.com/items?itemName=gencay.vscode-chatgpt)面向 ChatGPT 编程实现这段演示代码，代码生成后点击 Insert 自动插入代码到右侧编辑区：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled.png)

当然，你也可以从第三方云存储下载图片丰富代码实现细节：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%201.png)

除了具体代码外，你还可以让 ChatGPT 给出项目的通用目录结构（这也是代码框架的一部分）作为参考：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-6-882x1024.png)

## 1、代码解释

你可以拿出想要理解的任何代码，比如上面这段 ChatGPT 自动生成的图片下载代码，让 ChatGPT 对其进行解释：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%202.png)

可以看到这些解释非常详细，这比自己摸索试图理解复杂的代码要快得多，尤其是一些比较抽象的、封装度比较高的底层代码。比如[红黑树的实现代码](https://geekr.dev/posts/red-black-tree-implementation#toc-6)，我看不懂这段插入节点的代码，作者又没有写任何注释，可以让 ChatGPT 代劳：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-1024x1018.png)

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-1-1024x595.png)

## 2、改进现有的代码

通过描述你想要实现的目标，让 ChatGPT 对现有的代码进行改进。比如这里假设图片资源不存在，则退出不执行后面的文件保存操作：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%203.png)

它会为你提供如何实现目标的说明，包括修改后的代码，非常酷。

## 3、使用正确的命名规范重写代码

当重构由非本地 Go 开发人员编写的使用不同命名约定的代码时，这非常有用：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%204.png)

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%205.png)

注意到 ChatGPT 不仅为你提供更新后的代码，还解释了更改的原因。

## 4、使用正确的代码风格重写代码

当审查（Review）和重构（Rewrite）由非本地 Go 开发人员编写的代码时，这非常有帮助。ChatGPT 熟知 Go 语言代码风格，并将为你提供改进代码的建议，使其更易于阅读：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%206.png)

## 5、简化代码

我们还可以让 ChatGPT 简化复杂的代码，结果将是原始代码的更紧凑版本，比如我们让 ChatGPT 来简化这段[插入算法](https://geekr.dev/posts/go-sorting-algorithm-insertion)的示例代码：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%207.png)

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%208.png)

你可以对比运行下两段代码的运行结果，完全一致，但是 ChatGPT 提供的简化版本显然代码更加简洁。

## 6、编写测试用例

这已经成为我最喜欢的 ChatGPT 功能之一：询问它是否可以帮助你测试一个函数，它将为你编写测试用例。还是以上面这个插入排序函数为例：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%209.png)

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%2010.png)

Go 测试用例中一般是不包含 `main` 函数的，你可以让 ChatGPT 中去掉 `main` 函数：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%2011.png)

## 7、探索替代方案

有的时候，我们可能面对的是一段并不是性能最好的代码实现，比如基准测试后得出一段代码性能并不是很理想，需要寻求另一种更好的实现方式。这个时候，可以让 ChatGPT 给我们提供思路，当你想要探索不同的解决方案时，这非常有用。

下面以一段斐波那契数列的[递归实现](https://geekr.dev/posts/go-recursive-function-and-optimization)优化为例进行演示：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%2012.png)

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%2013.png)

这里 ChatGPT 给出了两种替代方案，都很靠谱。

## 8、翻译代码

每当你想要将某些代码从一种语言转换到另一种语言时，可以请求 ChatGPT 帮助翻译，这对它来说是小菜一碟：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%2014.png)

非常棒！

## 9、编写文档

这是我最喜欢的另一个技巧之一。询问 ChatGPT 编写代码的文档，它通常可以很好地完成。它甚至会将使用示例包括在文档中：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%2015.png)

## 10、调试代码&修复问题

如果你在代码中遇到困难并且找不到错误，可以向 ChatGPT 寻求帮助。它可能只需要几秒钟就能够找到错误原因所在。我不知道你的情况如何，但对我来说有时候会比 ChatGPT 要花费更长的时间。

我们以前面的下载图片为例进行演示：

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%2016.png)

![Untitled](https://image.gstatics.cn/2023/02/28/Untitled%2017.png)

不仅能找到问题，还能给出修复后的代码，调试代码的时间是不是大幅提升了呢？

当然，ChatGPT 也有不靠谱的时候，如果修复后的代码仍然存在问题，你也可以根据运行后的报错，进一步给 ChatGPT 进行提示，让它尝试给出更准确的答案，这部分之前主要是搜索引擎的使用场景，往后会随着 ChatGPT 的日益智能被逐步替代。

## 11、正则表达式

写正则表达式相信对很多开发者来说都是个很痛苦的事情，之前我们的做法通常是去搜索引擎搜索某个需求对应正则表达式的写法，然后去验证，虽然也有类似 [regex101](https://regex101.com/) 这样的网站提供集常见模式、构建、测试于一体的友好服务，但与 ChatGPT 这种能直接理解人类自然语言，同时又能嫁接和计算机沟通的机器人相比，显然后者更加高效直接：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-2-1024x666.png)

我觉得日后对于写正则表达式的需求，可以直接交给 ChatGPT 了，这比自己摸索测试要高效很多，又可以提前下班的一个小技巧。

## 12、学习新语言/技能

以上的演示都是在一个语言内部，现在，我们尝试把我们的视野放得更广一些，从 Go 语言到其他语言、到命令行、到前端、到数据库、到全栈开发。

学习一门新语言/框架/技术可以直接找 ChatGPT 给我们推荐相关的网站、博客、图片以及学习路线图。比如我想要学习 Rust：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-3-1024x758.png)

我们还可以就某个资源进一步提问，比如我想要了解《Rust 编程之道》这本书的目录结构和整体介绍：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-4-1024x649.png)

最后，我们还可以让 ChatGPT 给出 Rust 这门语言的学习路线图 —— 如何从入门到精通：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-5-1024x965.png)

非常棒。更多你感兴趣的问题，可以直接问 ChatGPT，我这里就不详细展开了。

## 13、命令行助手

### Bash 命令

日常开发/运维过程中，经常需要和各种终端命令打交道，有了 ChatGPT 后，就再也不用为这种琐碎的事情耗费精力了，比如我想要找到 Linux 系统下某个目录所有 jpg 文件，并输出文件名到文本文件，可以这么做：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-7-1024x558.png)

是不是非常高效直接？你可以问 ChatGPT 任何你需要的 Bash 命令的写法，堪称日常运维必备佳品，又一个可以提前下班的小技巧 Get。

当然，你也可以轻松将其转化为 Windows Dos 命令行的命令：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-8-1024x554.png)

### Git 命令

日常开发中另一个需要经常打交道的就是 Git 命令了，不过如果你日常使用的都是图形化的 Git 客户端，可能使用频率会低一些，和 Bash 命令一样，我们可以询问 ChatGPT 任何 Git 命令的写法：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-9-1024x890.png)

### Vi 命令

现在使用 Vi 编辑器的程序员很少了，但是在 Linux 系统上运维，有的时候还是难免需要用到几个 Vi 命令（Linux 默认编辑器就是 Vi），有了 ChatGPT 之后，这就很简单了，因为遇事不决问 ChatGPT 就好了：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-10-1024x659.png)

除了 Vi 编辑器外，各种 IDE 的快捷键也不在话下：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-11-1024x514.png)

ChatGPT 在手，那些各种命令行、快捷键的 Cheatsheet 以及桌面、桌垫都可以扔进垃圾桶了。

## 14、数据库助手

除了让 ChatGPT 帮我们编写各种命令行命令外，还可以让它帮我们生成各种 SQL 语句，这是程序员日常提效的另一个重要领域。

### 创建数据表

比如我想要构建一个博客网站，需要一张文章表：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-12-1024x740.png)

如果想要指定字段，可以这么做（作为一个 NLP 模型，ChatGPT 能够理解自然语言，没有任何格式约束）：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-13-1024x829.png)

可以为指定字段设置索引：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-14-1024x487.png)

### 插入假数据

数据表创建好了之后，可以为其填充一些假数据用于测试：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-15-1024x794.png)

如果想要通过代码插入，方便基于需求对数据进行调整，也可以让 ChatGPT 生成对应的代码，甚至指定使用的 ORM 框架，比如 `gorm`：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-16-1021x1024.png)

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-17-1006x1024.png)

### 查询数据表

有了数据之后，就可以对数据进行查询了，比如，我们想要在某个侧边栏展示浏览数最高的 10 篇文章：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-18-1024x611.png)

更复杂一点，我们需要在热门文章列表展示作者信息，这需要连表查询：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-19-1024x688.png)

非常棒，是不是？更新、删除这里就不一一演示了，你只需要通过自然语言提供你的需求，SQL 的事情让 ChatGPT 帮你完成即可，提前下班小技巧 +N。

## 15、HTML & CSS

有了后端和数据库之后，接下来向前端迈进，完成面向 ChatGPT 实现全栈开发的最后一环。让我们回到这篇教程的起点，从远程下载的图片最后需要在页面上展示，我们可以让 ChatGPT 帮我们实现对应的 HTML&CSS 代码：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-20-1024x922.png)

详细代码就不贴出来了，比较长，大家自己去体验就好了，我们可以去 [HTML Playgroud](https://playcode.io/html) 去体验下效果，看起来很不赖：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-21.png)

### Tailwind CSS

当然，如果你对 CSS 框架有要求，可以让 ChatGPT 轻松帮你完成转化工作：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-22-1024x882.png)

## 16、JavaScript

仅有 HTML&CSS 是没法和后端进行交互的，所以需要引入 JavaScript，不过，面向 ChatGPT 编程也无需感知这些技术层面的术语，只需要通过自然语言给它提需求就好。

比如，假设这个卡片对应的是视频网站列表的某个视频，鼠标移上去就会自动播放视频，我们直接把自然语言需求提供给 ChatGPT，它就会给我们生成对应的 JavaScript 实现代码：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-23-1024x767.png)

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-24-1024x950.png)

不仅给出了整体实现的思路和代码，还考虑到浏览器兼容性及对应的处理方式，非常棒。

### 与后端交互

这里并没有调用后端接口，完全是前端浏览器行为，为了保护视频原始链接，这里我们将其改造为从后端 API 接口获取视频链接：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-27-1024x596.png)

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-28-1024x665.png)

### Vue 组件

当然，和 CSS 一样，这里也可以使用流行的 JavaScript 框架来替换原生的实现代码，比如 Vue 或者 React，这里我们以 Vue 为例进行演示：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-29-1024x940.png)

完整代码这里就不贴出来了，感兴趣的同学可以自己去尝试。甚至你还可以通过 TypeScript 实现这段代码，只需要在需求中附加这个约束就好了。

## 17、面试准备

好了，至此，我想，我已经从前端、后端、数据库、Devops 等维度覆盖了面向 ChatGPT 编程实现全栈开发的方方面面，你已经具备成为 Prompt 工程师（面向 ChatGPT 编程就是 Prompt 驱动）的理论基础，勤加练习，就可以成为一名合格的 Prompt 工程师，接下来，就到了找工作的环节，在这个环节，我们仍然可以借助 ChatGPT 帮我们做好面试准备工作。

### 写简历

提供你的履历、技能、项目经验，让 ChatGPT 自动帮你生成简历：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-30-1024x839.png)

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-31-1024x959.png)

还不错，给我提供了基本的模板，然后我们稍加填充和润色就可以用了。

### 模拟面试

简历一旦通过筛选，就可以进入面试环节了，我们可以根据对应公司和岗位的要求（网上可以搜索到信息，或者咨询 ChatGPT 也可以），让 ChatGPT 给我们做模拟面试。

首先我们可以让 ChatGPT 帮我们生成面试问题：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-32-1024x369.png)

如果哪一题不会，可以立即问 ChatGPT：

![img](https://geekr.gstatics.cn/wp-content/uploads/2023/03/image-33-1024x951.png)

非常方便，有没有？你不妨可以试试看，通过 ChatGPT 准备一次面试，然后看看效果。

## 题外话

在面向 ChatGPT 编程的过程中，需要记住以下两点，这也是使用 ChatGPT 编程的两个大前提：

- 我拥有超过X年的编程经验，我知道我在做什么。
- 我不相信别人的代码（包括我的代码），我也不相信 ChatGPT 的输出。

使用 ChatGPT 不是说让它替我完成所有工作，使用 ChatGPT 是为了让我的产出和效率提升 10 倍。

ChatGPT 只是一个工具，而不是主导者，工具是给人使用的，能否最大化工具价值也在于使用它的人。主导者永远在人，在我。

何况，ChatGPT 也是有缺陷的。我发现它在处理代码时会出错，它不是总是对的，但这就是为什么我会在这里：监督它。我们一起形成了一个更完美的联盟。另外，那些诋毁这个工具的开发者正在忽略它的价值。

> OpenAI 还专门提供了 [Code API](https://platform.openai.com/docs/guides/code) 以帮助在自己的产品中集成代码生成和操作。需要说明的是本文基于 GPT3.5编写，新发布的GPT4在编码能力上更加强大，值得体验一下。

