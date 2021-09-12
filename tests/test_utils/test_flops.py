from models.arch import build_model
from utils import cfg, get_model_complexity_info, load_config


def test_flops():
    load_config(cfg, "./config/nanodet-m.yml")

    model = build_model(cfg.model)
    input_shape = (3, 320, 320)
    get_model_complexity_info(model, input_shape)
