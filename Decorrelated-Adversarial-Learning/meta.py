mixture = {
    'train_root': 'E:/2021WIN/SI681/Decorrelated-Adversarial-Learning/train_crop',
    'val_root': 'E:/2021WIN/SI681/Decorrelated-Adversarial-Learning/val_crop',
    'pat': '_|\.',
    'pos': 1,
    'n_cls': 1993
}

FGNET = {
    'train_root': '/data/fuzhuolin/cross_age/data/aligned_dlib_112x96/FGNET/train',
    'val_root': '/data/fuzhuolin/cross_age/data/aligned_dlib_112x96/FGNET/val',
    'pat': '_|\.',
    'pos': 1,
    'n_cls': 82
}

vgg_toy = {
    'train_root': '/data/fuzhuolin/cross_age/data/aligned_dlib_112x96/VGG_toy',
    'val_root': None,
    'pat': '_|\.',
    'pos': 1,
    'n_cls': 8
}

age_cutoffs = [12, 18, 25, 35, 45, 55, 65]