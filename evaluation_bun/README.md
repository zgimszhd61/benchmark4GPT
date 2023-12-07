使用bun语言HelloWorld
要在bun环境中编写并运行HelloWorld程序，你需要首先安装bun环境，然后创建一个JavaScript文件，最后在终端中运行这个文件。以下是具体的步骤：

1.  安装bun环境：bun是一个现代的JavaScript运行环境，类似于Node和Deno。它的执行速度往往要比V8等更传统引擎要快，因为它使用的是JavaScriptCore引擎，并且是由Zig语言编写而成的[1]。 
2.  创建JavaScript文件：在你的工作目录中，创建一个新的JavaScript文件，例如hello.js。在这个文件中，你可以编写以下代码来输出"Hello World"： 

export default {
  fetch(request) {
    return new Response("Hello World");
  },
};

这段代码定义了一个默认导出的对象，该对象有一个fetch方法，这个方法返回一个新的Response对象，其内容为"Hello World"[1]。

3. 在终端中运行文件：在终端中，你可以使用bun run命令来运行你的JavaScript文件。例如，如果你的文件名为hello.js，你可以运行以下命令：

bun run hello.js

然后，你可以在浏览器中打开http://localhost:3000/，你应该能看到"Hello World"的输出[1]。

请注意，bun环境的配置文件为bunfig.toml，你可以在这个文件中进行一些配置，例如设置日志级别、公共目录等[1]。

Citations:
[1] https://www.cnblogs.com/Grewer/p/16534170.html
[2] https://www.oschina.net/news/213986/bun-0-2-0-released
[3] https://blog.csdn.net/qiwoo_weekly/article/details/131650909
[4] https://cloud.tencent.com/developer/article/1836840?areaId=106001
[5] https://www.infoq.cn/article/tqy53cjovuy8gak4v9we
[6] https://juejin.cn/post/6983237935638249509
[7] https://cloud.tencent.com/developer/article/2331178?areaId=106005
[8] https://blog.michealwayne.cn/2022/07/17/notes/【笔记】越来越快的jsRuntime——Bun/
[9] https://cloud.tencent.com/developer/article/2251081
[10] https://163.com/dy/article/HFC8JOHO0553SRCA.html?spss=adap_pc
[11] https://www.oschina.net/news/259198/bun-1-0-3-released
