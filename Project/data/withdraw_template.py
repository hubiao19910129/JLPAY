# -*- coding: utf-8 -*-
#提现提交申请
withdrawApply = {
    "command_id":"withdrawApply",
    "s_user_id":"",   #要获取的代理商ID--必输项
    "amount":"",      #金额--必输项
    "subject":"1001",
    "logId":"docapi_logId",
    "s_user_id":"",
    "s_user_name":"",
    "operatorId":""
}

#提现审核
withdrawAudit = {
    "command_id":"withdrawAudit",
    "s_user_id":"",   #审核人-代理商ID---必输项
    "withdrawId":"",  #提现记录ID--必输项
    "status":"",      #审核状态: 0=不通过，1=通过，2=挂账--必输项
    "reason":"",      #不通过的原因，status = 0时必须
    "logId":"docapi_logId",
    "s_user_id":"",
    "s_user_name":"",
    "operatorId":""
}

#营销账户 提现提交申请
withdrawMarketApply = {
    "command_id":"withdrawMarketApply",
    "s_user_id":"",      #要获取的代理商ID--必输项
    "amount":"",         #提现金额，单位：分--必输项
    "logId":"docapi_logId",
    "s_user_id":"",
    "s_user_name":"",
    "operatorId":""
}

#提现付款
withdrawPayRpc = {
    "command_id":"withdrawPayRpc",
    "withdrawId":"",  #提现ID--必输项
    "repay":"",       #重新付款标识 1-重新付款 0-首次付款 默认为0
    "logId":"docapi_logId",
    "s_user_id":"861",
    "s_user_name":"王云洲",
    "operatorId":"861",
}

#批量提现代付
withdrawBatchPayRpc = {
    "command_id":"withdrawBatchPayRpc",
    "withdrawIds":"",   #提现ID列表；列表类型 ["id1", "id2"]--必输项
    "logId":"docapi_logId",
    "s_user_id":"861",
    "s_user_name":"王云洲",
    "operatorId":"861"
}

#提现代付结果查询
withdrawPayQueryRpc = {
    "command_id":"withdrawPayQueryRpc",
    "withdrawId":"",        #提现ID--必输项
    "logId":"docapi_logId",
    "s_user_id":"861",
    "s_user_name":"王云洲",
    "operatorId":"861"
}

