##! drupal rce detection.

@load base/protocols/http/main.zeek
@load base/frameworks/notice

export {
    redef enum Notice::Type += {
        Attack_RCE,
    };
}
event tcp_packet(c: connection, is_orig: bool, flags: string, seq: count, ack: count, len: count, payload: string)
{	

    if (is_orig && "form_id=user_register_form" in payload && "_drupal_ajax=1" in payload)
    {
        local rce = "detect rce attack";
        print(rce);
        local n: Notice::Info = Notice::Info($note=Attack_RCE, 
                                            $msg="druapl RCE attack", 
                                            $sub=payload,
                                            $conn=c);
    	NOTICE(n);
    }
}
