""" Constants for prepackaged models of introspective rationale explainer """

BERT_MODEL_CONFIG = {
    "cuda": False,
    "pretrain_cls": False,
    "batch_size": 32,
    "num_epochs": 1,
    "num_pretrain_epochs": 10,
    "save_best_model": False,
    "hidden_dim": 768,
    "embedding_dimension": 768,
    "gen_embedding_dim": 768,
    "label_embedding_dim": 400,
    "fixed_classifier": False,
    "lambda_sparsity": 1.0,
    "lambda_continuity": 0,
    "lambda_anti": 1.0,
    "target_sparsity": 0.3,
    "training_stop_thresh": 5,
    "count_pieces": 4,
    "fine_tuning": True,
    "bert_explainers": True,
    "dropout_rate": 0.3,
    "layer_num": 1,
    "embedding_dim": 100,
    "exploration_rate": 0.05,
    "lambda_acc_gap": 1.2,
    "lr": 2e-4,
    "train_batch_size": 32,
    "test_batch_size": 32,
    "model_save_dir": '..\\test_models',
    "model_prefix": 'sst2rnpmodeltest',
    "embedding_path": '../../../data/sst2\\',
    "labels": [0, 1],
    "num_labels": 2
}

BERT_RNN_MODEL_CONFIG = {
    "cuda": False,
    "pretrain_cls": False,
    "batch_size": 32,
    "num_epochs": 1,
    "num_pretrain_epochs": 10,
    "save_best_model": False,
    "hidden_dim": 100,
    "embedding_dimension": 100,
    "gen_embedding_dim": 100,
    "label_embedding_dim": 400,
    "fixed_classifier":False,
    "lambda_sparsity": 1.0,
    "lambda_continuity": 0,
    "lambda_anti": 1.0,
    "target_sparsity": 0.3,
    "training_stop_thresh": 5,
    "count_pieces": 4,
    "fine_tuning": True,
    "bert_explainers": False,
    "dropout_rate": 0.3,
    "layer_num": 1,
    "embedding_dim": 100,
    "exploration_rate": 0.05,
    "lambda_acc_gap": 1.2,
    "lr": 2e-4,
    "train_batch_size": 32,
    "test_batch_size": 32,
    "model_save_dir": '..\\test_models',
    "model_prefix": 'sst2rnpmodeltest',
    "embedding_path": '../../../data/sst2\\',
    "labels": [0, 1],
    "num_labels": 2
}

RNN_MODEL_CONFIG = {
    "cuda": False,
    "pretrain_cls": False,
    "batch_size": 32,
    "num_epochs": 1,
    "num_pretrain_epochs": 10,
    "save_best_model": False,
    "hidden_dim": 100,
    "embedding_dimension": 100,
    "gen_embedding_dim": 100,
    "label_embedding_dim": 400,
    "fixed_classifier":False,
    "lambda_sparsity": 1.0,
    "lambda_continuity": 0,
    "lambda_anti": 1.0,
    "target_sparsity": 0.3,
    "training_stop_thresh": 5,
    "count_pieces": 4,
    "fine_tuning": True,
    "bert_explainers": False,
    "dropout_rate": 0.3,
    "layer_num": 1,
    "embedding_dim": 100,
    "exploration_rate": 0.05,
    "lambda_acc_gap": 1.2,
    "lr": 2e-4,
    "train_batch_size": 32,
    "test_batch_size": 32,
    "model_save_dir": '..\\test_models',
    "model_prefix": 'sst2rnpmodeltest',
    "embedding_path": '../../../data/sst2\\',
    "labels": [0, 1],
    "num_labels": 2
}