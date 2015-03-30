# !/usr/bin/env python
# -*- coding: utf-8 -*-

# class User(Model):
# 	# 定义类的属性到列的映射
# 	id = IntegerField('id')
# 	name = StringField('username')
# 	email = StringField('email')
# 	password = StringField('password')

# # 创建一个实例:
# u = User(id=12345, name='Micheal', email='test@orm.org', password='my-pwd')
# # 保存到数据库:
# u.save()

class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return '<%s: %s>' % (self.__class__.__name__, self.name)

class StringField(Field):
	"""docstring for StringField"""
		def __init__(self, name):
			super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	"""docstring for Inter"""
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')
		self.arg = arg
		
class ModeMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name=='Model':
			return type.__new__(cls, name, bases, attrs)
		mappings = dict()
		for k, v in attrs.iteritems():
			if isinstance(v, Field):
				print('Found mapping: %s==>%s' % (k, v))
				mappings[k] = v
		for k in mappings.iterkeys():
			attrs.pop(k)
		attrs['__table__'] = name 
		attrs['__mappings__'] = mappings
		return type.__new__(cls, name, bases, attrs)

class Model(dict):
	__metaclass__ = ModeMetaclass

	def __getattr(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
		
	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.iteritems():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))

		