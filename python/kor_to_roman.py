# -*- coding: utf-8 -*-
import string

c_base = 44032
cho_base = 4352
jung_base = 4449
jong_base = 4519

# 초성 리스트. 00 ~ 18
CHO_LIST = [u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

# 중성 리스트. 00 ~ 20
JUNG_LIST = [u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ', u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ']

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONG_LIST = [u' ', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ', u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

cho_u = {4352: 'ㄱ', 4353: 'ㄲ', 4354: 'ㄴ', 4355: 'ㄷ', 4356: 'ㄸ', 4357: 'ㄹ', 4358: 'ㅁ', 4359: 'ㅂ', 4360: 'ㅃ', 4361: 'ㅅ', 4362: 'ㅆ', 4363: 'ㅇ', 4364: 'ㅈ', 4365: 'ㅉ', 4366: 'ㅊ', 4367: 'ㅋ', 4368: 'ㅌ', 4369: 'ㅍ', 4370: 'ㅎ'}

jung_u = {4449: 'ㅏ', 4450: 'ㅐ', 4451: 'ㅑ', 4452: 'ㅒ', 4453: 'ㅓ', 4454: 'ㅔ', 4455: 'ㅕ', 4456: 'ㅖ', 4457: 'ㅗ', 4458: 'ㅘ', 4459: 'ㅙ', 4460: 'ㅚ', 4461: 'ㅛ', 4462: 'ㅜ', 4463: 'ㅝ', 4464: 'ㅞ', 4465: 'ㅟ', 4466: 'ㅠ', 4467: 'ㅡ', 4468: 'ㅢ', 4469: 'ㅣ'}

jong_u = {4520: 'ㄱ', 4521: 'ㄲ', 4522: 'ㄳ', 4523: 'ㄴ', 4524: 'ㄵ', 4525: 'ㄶ', 4526: 'ㄷ', 4527: 'ㄹ', 4528: 'ㄺ', 4529: 'ㄻ', 4530: 'ㄼ', 4531: 'ㄽ', 4532: 'ㄾ', 4533: 'ㄿ', 4534: 'ㅀ', 4535: 'ㅁ', 4536: 'ㅂ', 4537: 'ㅄ', 4538: 'ㅅ', 4539: 'ㅆ', 4540: 'ㅇ', 4541: 'ㅈ', 4542: 'ㅊ', 4543: 'ㅋ', 4544: 'ㅌ', 4545: 'ㅍ', 4546: 'ㅎ'}

dic_cho = {'ㄱ': 'g', 'ㄲ': 'gg', 'ㄴ': 'n', 'ㄷ': 'd', 'ㄸ': 'dd', 'ㄹ': 'r', 'ㅁ': 'm', 'ㅂ': 'b', 'ㅃ': 'pp', 'ㅅ': 's', 'ㅆ': 'ss', 'ㅇ': '', 'ㅈ': 'j', 'ㅉ': 'jj', 'ㅊ': 'c', 'ㅋ': 'k', 'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 'h'}

dic_jung =  {'ㅏ': 'a', 'ㅐ': 'ae', 'ㅑ': 'ya', 'ㅒ': 'yae', 'ㅓ': 'eo', 'ㅔ': 'e', 'ㅕ': 'yeo', 'ㅖ': 'yeo', 'ㅗ': 'o', 'ㅘ': 'wa', 'ㅙ': 'wae', 'ㅚ': 'oe', 'ㅛ': 'yo', 'ㅜ': 'u', 'ㅝ': 'weo', 'ㅞ': 'weo', 'ㅟ': 'wi', 'ㅠ': 'yu', 'ㅡ': 'eu', 'ㅢ': 'ui', 'ㅣ': 'i'}

dic_jong = {'ㄱ': 'k', 'ㄲ': 'kk', 'ㄳ': 'gs', 'ㄴ': 'n', 'ㄵ': 'nj', 'ㄶ': 'nh', 'ㄷ': 't', 'ㄹ': 'l', 'ㄺ': 'lg', 'ㄻ': 'lm', 'ㄼ': 'lb', 'ㄽ': 'ls', 'ㄾ': 'lt', 'ㄿ': 'lp', 'ㅀ': 'lh', 'ㅁ': 'm', 'ㅂ': 'p', 'ㅄ': 'bs', 'ㅅ': 's', 'ㅆ': 'ss', 'ㅇ': 'ng', 'ㅈ': 'j', 'ㅊ': 'c', 'ㅋ': 'k', 'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 'h'}



def split(raw):
	final = []
	dic = ''
	han = ['cho','jung','jong']
	for i,char in enumerate(raw,1):
		if ord(char) >= c_base:
			c = ord(char)
			c = c - c_base
			jong = c % 28
			jung = ((c - jong ) / 28) % 21
			cho = (((c - jong ) / 28) - jung) / 21
			# 초 중 종
			a = getValue(cho_u,int(cho_base+cho))
			b = getValue(jung_u,int(jung_base+jung))
			c = getValue(jong_u,int(jong_base+jong))
			dic = dict(zip(han, [a,b,c]))
			final.append(dic)
		elif char.isspace(): 
			final.append({'N': ' '})
		else:
			final.append({'N': char})
	return final

def combine(input):
	list = input.split(' ')
	
	cho, jung, jong = 0, 0, 0 
	
	if len(list) is 3:
		try:
			cho = CHO_LIST.index(list[0])
			jung = JUNG_LIST.index(list[1])
			jong = JONG_LIST.index(list[2])
		except Exception as e:
			print('Character not in list')
			return input
	elif len(list) is 2: 
		try:
			cho = CHO_LIST.index(list[0])
			jung = JUNG_LIST.index(list[1])
		except Exception as e:
			print('Character not in list')
			return input
	else:
		print('Not Valid')
		return input
	
	c = (21*cho + jung) * 28 + jong + c_base
	print(c)
	return chr(c)
	
def getValue(dic, input):
	if input in dic:
		return dic[input]
	return ''
	
def translate(list):
	str = ''
	for dic in list:
		if type(dic) is dict:
			str += getValue(dic_cho, getValue(dic, 'cho'))
			str += getValue(dic_jung, getValue(dic, 'jung'))
			str += getValue(dic_jong, getValue(dic, 'jong'))
			str += getValue(dic, 'N')
		else:
			str += dic
	return string.capwords(str.rstrip())
	
while True:
	x = input('input: ')
	print('split: ', split(x))
	print('번역: ',translate(split(x)))

	y = input('input(초,중,종성): ')
	print(combine(y))
