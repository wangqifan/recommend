package com.wangqifan.webservice.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.List;


@Service
public class recommendservice implements recommendserviceinter {
    @Autowired
    private recommendclient client;

    @Override
    public List<Integer> getmoviesid(int userid)
    {
       return client.getmovieid(userid);
    }
}
