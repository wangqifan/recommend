package com.wangqifan.webservice;


import com.alibaba.fastjson.JSON;
import com.wangqifan.webservice.base.ApiResponse;
import com.wangqifan.webservice.service.recommendclient;
import com.wangqifan.webservice.service.recommendserviceinter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import javax.swing.event.ListDataEvent;
import java.util.List;

@RestController
public class RecommendController {

    @Autowired
    private recommendserviceinter recommend;


    @GetMapping("/recommend/{userid}")
    String recommend(@PathVariable("userid") int userid)
    {
        try {
            List<Integer> list = recommend.getmoviesid(userid);
            String jsonstr = JSON.toJSONString(list);
            return JSON.toJSONString(ApiResponse.ofMessage(200,jsonstr));
        }
        catch (Exception e)
        {
            return JSON.toJSONString(ApiResponse.ofMessage(500,"服务器出错"));
        }

    }
}
