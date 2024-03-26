from emlakVeriCekme import EmlakVerileri
from formDoldurma import FormDolduran

emlak = EmlakVerileri()
emlak.getLinks()
emlak.getAddress()
emlak.getPrices()
emlak.setJson()

google_form = FormDolduran()
google_form.setForm(emlak.JSON)
