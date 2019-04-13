# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2019/4/4.
  「pay接口」只能用户访问，CMS管理员不能反问
"""
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.validators.params import IDMustBePositiveInt
from app.api_docs import pay as api_doc

__author__ = 'Alimazing'

api = RedPrint(name='pay', description='支付', api_doc=api_doc)

@api.route('pre_order', methods=['POST'])
@api.doc()
@auth.login_required
def get_pre_order():
	'''获取预订单'''
	id = IDMustBePositiveInt().validate_for_api().id.data
	pass
