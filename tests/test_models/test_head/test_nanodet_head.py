import torch

from models.head import build_head
from utils.yacs import CfgNode


def test_gfl_head_loss():
    head_cfg = dict(
        name="NanoDetHead",
        num_classes=80,
        input_channel=1,
        feat_channels=96,
        stacked_convs=2,
        conv_type="DWConv",
        reg_max=8,
        strides=[8, 16, 32],
        loss=dict(
            loss_qfl=dict(
                name="QualityFocalLoss", use_sigmoid=True, beta=2.0, loss_weight=1.0
            ),
            loss_dfl=dict(name="DistributionFocalLoss", loss_weight=0.25),
            loss_bbox=dict(name="GIoULoss", loss_weight=2.0),
        ),
    )
    cfg = CfgNode(head_cfg)

    head = build_head(cfg)
    feat = [torch.rand(1, 1, 320 // stride, 320 // stride) for stride in [8, 16, 32]]

    cls_preds, reg_preds = head.forward(feat)
    for cls, reg, stride in zip(cls_preds, reg_preds, [8, 16, 32]):
        assert cls.shape == (1, 80, 320 // stride, 320 // stride)
        assert reg.shape == (1, (8 + 1) * 4, 320 // stride, 320 // stride)

    head_cfg = dict(
        name="NanoDetHead",
        num_classes=20,
        input_channel=1,
        feat_channels=96,
        stacked_convs=2,
        conv_type="Conv",
        reg_max=5,
        share_cls_reg=False,
        strides=[8, 16, 32],
        loss=dict(
            loss_qfl=dict(
                name="QualityFocalLoss", use_sigmoid=True, beta=2.0, loss_weight=1.0
            ),
            loss_dfl=dict(name="DistributionFocalLoss", loss_weight=0.25),
            loss_bbox=dict(name="GIoULoss", loss_weight=2.0),
        ),
    )
    cfg = CfgNode(head_cfg)
    head = build_head(cfg)

    cls_preds, reg_preds = head.forward(feat)
    for cls, reg, stride in zip(cls_preds, reg_preds, [8, 16, 32]):
        assert cls.shape == (1, 20, 320 // stride, 320 // stride)
        assert reg.shape == (1, (5 + 1) * 4, 320 // stride, 320 // stride)
