from django import forms

class ProdukMakananForm(forms.Form):
    id_produk_makanan = forms.CharField(label='ID Produk Makanan', max_length=50)
    jumlah = forms.IntegerField(label='Jumlah', max_length=50)