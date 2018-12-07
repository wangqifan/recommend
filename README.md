# recommend
数字图书馆作业


依赖
-----
  * java运用程序依赖见pom.xml
  * python应用程序需要安装flask
 
运行
------
   * 运行服务注册中心
  
    java -jar eureka-server-0.0.1-SNAPSHOT.jar
    
   * 运行webservice 
    
    java -jar webservice-0.0.1-SNAPSHOT.jar
    
    
    * 运行推荐服务
    
    python run.py
    
    
    *运行情感分析服务
    
    python  analyseserver.py
    
    
备注
---
还需要安装redis
