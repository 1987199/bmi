height = input('请输入身高cm: ')
weight = input('请输入体重kg: ')
height = float(height)
weight = float(weight)
height = height / 100 #换成公尺
BMI = weight / height / height
print('您的BMI值为: ', BMI)
if BMI < 18.5:
	print('体重过轻')
elif BMI >= 18.5 and BMI < 24:
	print('体重正常')
elif BMI >= 24 and BMI < 27:
	print('稍重')
elif BMI >=27 and BMI < 30:
	print('轻度肥胖')
elif BMI >= 30 and BMI < 35:
	print('中度肥胖')
else:
	print('重度肥胖')