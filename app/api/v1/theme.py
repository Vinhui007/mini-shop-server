# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/17.
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.theme import Theme
from app.validators.params import IDCollection, IDMustBePositiveInt
from app.api_docs import theme as api_doc

__author__ = 'Alimazing'

api = RedPrint(name='theme', description='主题', api_doc=api_doc)

@api.route('', methods=['GET'])
@api.doc()
def get_simple_list():
	'''一组 ID 的专题(Theme)
	:arg /theme?ids=id1,id2,id3,...
	:return: 一组theme模型
	'''
	ids = IDCollection().validate_for_api().ids.data
	theme = Theme.get_themes(ids=ids)
	return Success(theme)


@api.route('/<int:id>', methods=['GET'])
@api.doc()
def get_complex_one(id):
	'''专题(Theme)详情接口
	:param id: 专题theme的id
	:return: 专题theme的详情
	'''
	id = IDMustBePositiveInt().validate_for_api().id.data
	theme_detail = Theme.get_theme_detail(id=id)
	return Success(theme_detail)
