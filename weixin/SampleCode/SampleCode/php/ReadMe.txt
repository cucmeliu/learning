<?php
//װ��ģ���ļ�
include_once("wx_tpl.php");

//��ȡ΢�ŷ�������
$postStr = $GLOBALS["HTTP_RAW_POST_DATA"];

  //���ػظ�����
if (!empty($postStr)){

        //��������
          $postObj = simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);
        //������Ϣ��ID
          $fromUsername = $postObj->FromUserName;
        //������Ϣ��ID
          $toUsername = $postObj->ToUserName;
         //��Ϣ����
          $form_MsgType = $postObj->MsgType;

        //�¼���Ϣ
          if($form_MsgType=="event")
          {
            //��ȡ�¼�����
            $form_Event = $postObj->Event;
            //�����¼�
            if($form_Event=="subscribe")
            {
              //�ظ���ӭ������Ϣ
              $msgType = "text";
              $contentStr = "��л����ע�ƺ������ң�[���]\n\n������0�鿴�˵���[õ��]";
              $resultStr = sprintf($textTpl, $fromUsername, $toUsername, time(), $msgType, $contentStr);
             echo $resultStr;
              exit;
            }

          }

  }
  else
  {
          echo "";
          exit;
  }

?>