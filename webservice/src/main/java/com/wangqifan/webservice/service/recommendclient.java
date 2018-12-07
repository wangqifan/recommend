package com.wangqifan.webservice.service;


import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;

@FeignClient("recommend-service")
public interface recommendclient {
    @GetMapping("/recommend/{userid}")
    List<Integer> getmovieid(@PathVariable("userid")int userid);
}
