package com.wangqifan.webservice;


import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.wangqifan.webservice.base.ApiResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class CommentController {
    @Autowired
    private JedisAdapter jedisAdapter;


    @RequestMapping(path = {"/comment/"}, method = {RequestMethod.GET, RequestMethod.POST})
    String AddComment(@RequestParam("userId") int userid, @RequestParam("movieid") int movieid, @RequestParam("content") String content)
    {
        try {
            JSONObject json = new JSONObject();
            json.put("userid",userid);
            json.put("movieid",movieid);
            json.put("content",content);
            String str=json.toJSONString();
            jedisAdapter.lpush("comment", str);
            return JSON.toJSONString(ApiResponse.ofMessage(200,"评论成功"));
        }
        catch(Exception e)
        {
            return JSON.toJSONString(ApiResponse.ofMessage(500,"评论失败"));
        }
    }
}
