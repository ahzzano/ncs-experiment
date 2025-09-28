import openvino as ov

ov_model = ov.convert_model('squeeze_base')
ov.save_model(ov_model, 'ov_model.xml')
