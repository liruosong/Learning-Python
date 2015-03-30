# !/usr/bin/env python
# -*- coding: utf-8 -*-

# metaclass是创建类， 所以必须从'type'类型派生：
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(vaule)
		return type.__new__(cls, name, bases, attrs)

class MyList(list):
	__metaclass__ = ListMetaclass