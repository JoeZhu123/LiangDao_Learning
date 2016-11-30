__author__='Joe'
#._*_coding:utf-8_*_
#mdl getdata class
import os
import sys
sys.path.append("/home/calc4/Desktop/zhuxinger/mdl-1.7.0/mdl_client_api/redis_protocol/demo/python/")#mdl module directory

import csv
import time
import redis
import datetime
import mdl_shl1_msg_pb2
import mdl_szl1_msg_pb2



class mdl_LiangDao_GetData(object):
        def __init__(self):
            reload(sys)
            sys.setdefaultencoding('utf-8')

	def mdl_time_str(self,x):
		return "%02d:%02d:%02d.%03d" % (x % 1000000000 / 10000000, x % 10000000 / 100000, x % 100000 / 1000, x % 1000)

	def mdl_float_str(self,x):
		return "%f" % (x.Value / float(x.DecimalShift))

	def mdl_int_str(self,x):
		return "%d" % (x)

	def on_shl1_indexes_msg(self,data):
		msg = mdl_shl1_msg_pb2.Indexes()
		msg.ParseFromString(data)
		print "%s XSHG.%s %s: %s" % (self.mdl_time_str(msg.UpdateTime), msg.IndexID, msg.IndexName, self.mdl_float_str(msg.LastIndex))
		temp_data=[self.mdl_time_str(msg.UpdateTime),msg.IndexID,msg.IndexName,self.mdl_float_str(msg.PreCloseIndex),self.mdl_float_str(msg.OpenIndex),self.mdl_float_str(msg.Turnover),self.mdl_float_str(msg.HighIndex),self.mdl_float_str(msg.LowIndex),self.mdl_float_str(msg.LastIndex),self.mdl_int_str(msg.TradVolume),self.mdl_float_str(msg.CloseIndex),msg.TradingPhaseCode]#
		return temp_data

	def on_shl1_equity_msg(self,data):
		msg = mdl_shl1_msg_pb2.Equity()
		msg.ParseFromString(data)
		print "%s XSHG.%s %s: %s" % (self.mdl_time_str(msg.UpdateTime), msg.SecurityID, msg.SecurityName, self.mdl_float_str(msg.LastPrice))
		temp_data=[self.mdl_time_str(msg.UpdateTime),msg.SecurityID,msg.SecurityName,msg.TradingPhaseCode,self.mdl_float_str(msg.PreCloPrice),self.mdl_float_str(msg.OpenPrice),self.mdl_float_str(msg.Turnover),self.mdl_float_str(msg.HighPrice),self.mdl_float_str(msg.LowPrice),self.mdl_float_str(msg.LastPrice),self.mdl_float_str(msg.ClosePrice),self.mdl_int_str(msg.Volume)]#msg.BidPriceLevel,msg.AskPriceLevel
		return temp_data

	def on_szl1_stock_msg(self,data):
		msg = mdl_szl1_msg_pb2.SZL1Stock()
		msg.ParseFromString(data)#item['data']
		print "%s XSHE.%s %s: %s" % (self.mdl_time_str(msg.UpdateTime), msg.SecurityID, msg.SecurityName, self.mdl_float_str(msg.LastPrice))
		temp_data=[self.mdl_time_str(msg.UpdateTime),msg.SecurityID,msg.SecurityName,self.mdl_float_str(msg.PreCloPrice),self.mdl_float_str(msg.OpenPrice),self.mdl_float_str(msg.Turnover),self.mdl_float_str(msg.HighPrice),self.mdl_float_str(msg.LowPrice),self.mdl_float_str(msg.LastPrice),self.mdl_int_str(msg.Volume),self.mdl_int_str(msg.TurnNum),self.mdl_float_str(msg.PE1),self.mdl_float_str(msg.PE2),self.mdl_float_str(msg.DifPrice1),self.mdl_float_str(msg.DifPrice2),self.mdl_int_str(msg.BidVolume1),self.mdl_float_str(msg.BidPrice1),self.mdl_int_str(msg.BidVolume2),self.mdl_float_str(msg.BidPrice2),self.mdl_int_str(msg.BidVolume3),self.mdl_float_str(msg.BidPrice3),self.mdl_int_str(msg.BidVolume4),self.mdl_float_str(msg.BidPrice4),self.mdl_int_str(msg.BidVolume5),self.mdl_float_str(msg.BidPrice5),self.mdl_int_str(msg.AskVolume1),self.mdl_float_str(msg.AskPrice1),self.mdl_int_str(msg.AskVolume2),self.mdl_float_str(msg.AskPrice2),self.mdl_int_str(msg.AskVolume3),self.mdl_float_str(msg.AskPrice3),self.mdl_int_str(msg.AskVolume4),self.mdl_float_str(msg.AskPrice4),self.mdl_int_str(msg.AskVolume5),self.mdl_float_str(msg.AskPrice5),self.mdl_int_str(msg.DeletionIndicator)]#
		return temp_data

	def on_szl1_index_msg(self,data):
		msg = mdl_szl1_msg_pb2.SZL1Index()
		msg.ParseFromString(data)
		print "%s XSHE.%s %s: %s" % (self.mdl_time_str(msg.UpdateTime), msg.IndexID, msg.IndexName, self.mdl_float_str(msg.LastIndex))
		temp_data=[self.mdl_time_str(msg.UpdateTime),msg.IndexID,msg.IndexName,self.mdl_float_str(msg.PreCloseIndex),self.mdl_float_str(msg.OpenIndex),self.mdl_float_str(msg.Turnover),self.mdl_float_str(msg.HighIndex),self.mdl_float_str(msg.LowIndex),self.mdl_float_str(msg.LastIndex),self.mdl_int_str(msg.TradeVolume)]
		return temp_data


	#save data into txt files
	def saveData(self,dir_name,items):
		f=open(dir_name,"a+")
		f.write(items)
		f.close()
		return

	#save data into csv files
	def savecsv(self,dir_name,items,DataHead):
		if os.path.exists(dir_name+'.csv')==False:
			csvfile=open(dir_name+'.csv','a+')
			writer=csv.writer(csvfile)
			writer.writerow(DataHead)
		else:
			csvfile=open(dir_name+'.csv','a+')
			writer=csv.writer(csvfile)
			writer.writerow(items)
		csvfile.close()
		return 
	def getcsv(self):
		print "connect to redis..."
        r = redis.Redis(host='xxx.xxx.x.xxx', port=xxxx, db=0)#xxx.xxx.x.xxx为通联的IP，xxxx为端口
		if r.execute_command('auth', 'mytoken') :
			print "redis auth succeeded"
		else :
			print "redis auth failed"
			sys.exit()
		p = r.pubsub()
		p.subscribe(['mdl.3.3.000001', 'mdl.3.4.603600', 'mdl.5.2.*', 'mdl.2.4.*'])

		today=datetime.date.today()
		today_f=today.strftime("%Y%m%d")

		if os.path.exists('./'+today_f)==False:
			 os.mkdir(('./'+today_f+'/'))
		if os.path.exists('./'+today_f+'/Stock')==False:
			 os.mkdir(('./'+today_f+'/Stock/'))
		if os.path.exists('./'+today_f+'/Index')==False:
			 os.mkdir(('./'+today_f+'/Index/'))

		print "receiving message..."
		for item in p.listen(): 
                        today_Now_Time=time.strftime("%H%M",time.localtime(time.time()))
			if today_Now_Time == '1130' or today_Now_Time == '1500':
				print "Trade End!"
				break;
			if str(item['type']) == 'message':
				channel = str(item['channel'])
				if channel[0:8] == "mdl.3.3.":
					items=self.on_shl1_indexes_msg(item['data'])
					data_head=['UpdateTime','IndexID','IndexName','PreCloseIndex','OpenIndex','Turnover',
		'HighIndex','LowIndex','LastIndex','TradVolume','CloseIndex','TradingPhaseCode']
					self.savecsv(('./'+today_f+'/Index/'+'SH'+items[1]),items,data_head)
				elif channel[0:8] == "mdl.3.4.":
					items=self.on_shl1_equity_msg(item['data'])
					data_head=['UpdateTime','SecurityID','SecurityName','TradingPhaseCode','PreCloPrice','OpenPrice','Turnover',
		'HighPrice','LowPrice','LastPrice','ClosePrice','Volume']
					self.savecsv(('./'+today_f+'/Stock/'+'SH'+items[1]),items,data_head)
				elif channel[0:8] == "mdl.5.1.":
					items=self.on_szl1_index_msg(item['data'])
					data_head=['UpdateTime','IndexID','IndexName','PreCloseIndex','OpenIndex','Turnover',
		'HighIndex','LowIndex','LastIndex','TradVolume']
					self.savecsv(('./'+today_f+'/Index/'+'SZ'+items[1]),items,data_head)
				elif channel[0:8] == "mdl.5.2.":
					items=self.on_szl1_stock_msg(item['data'])
					data_head=['UpdateTime','SecurityID','SecurityName','PreCloPrice','OpenPrice','Turnover',
		'HighPrice','LowPrice','LastPrice','Volume','TurnNum','PE1','PE2','DifPrice1','DifPrice2','BidVolume1'
		,'BidPrice1','BidVolume2','BidPrice2','BidVolume3','BidPrice3','BidVolume4','BidPrice4','BidVolume5',
		'BidPrice5','AskVolume1','AskPrice1','AskVolume2','AskPrice2','AskVolume3','AskPrice3',
		'AskVolume4','AskPrice4','AskVolume5','AskPrice5','DeletionIndicator']
					self.savecsv(('./'+today_f+'/Stock/'+'SZ'+items[1]),items,data_head)
				elif channel[0:8] == "mdl.2.4.":
					print "heart beat"                        
				else:
					print "unknown channel: %s" % (channel)
                return
