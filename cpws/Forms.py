from django import forms


class CpwsForm(forms.Form):
    fymc = forms.CharField(max_length=50, label='法院名称')
    wslb = forms.ChoiceField(choices=[(1, '民事案件'), (2, '刑事案件'), (3, '行政案件'), (4, '执行案件'), (5, '赔偿案件')])
    bt = forms.CharField(max_length=200, label='标题')
    fbr = forms.CharField(max_length=10, label='发布人')
    nr = forms.CharField(widget=forms.Textarea, label='内容')

