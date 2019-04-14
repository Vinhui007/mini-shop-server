# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
__author__ = 'Allen7D'

from enum import Enum


class ClientTypeEnum(Enum):
	USER_EMAIL = 100
	USER_MOBILE = 101

	# 微信小程序
	USER_MINA = 200
	# 微信公众号
	USER_WX = 201


class ScopeEnum(Enum):
	'''
	「可读性」
	逻辑：数字越大，权限越大
	用法：ScopeEnum.User == ScopeEnum(1) # True
	'''
	User = 1 # 普通用户
	Admin = 2 # 管理员
	Super = 3 # 超级管理员

class OrderStatusEnum(Enum):
	UNPAID = 1 # 待支付
	PAID = 2 # 已支付
	DELIVERED = 3 # 已发货
	PAID_BUT_OUT_OF = 4 # 已支付，但库存不足