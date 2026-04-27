import subprocess
import sys
'''
COMMANDS=['Python -u run.py --is_training 1 --model_id AluminumAnode --model Informer --data AED --root_path '
          '"D:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',
          'Python -u run.py --is_training 1 --model_id AluminumAnode --model Informer --data AED --root_path '
          '"D:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',
          'Python -u run.py --is_training 1 --model_id AluminumAnode --model Informer --data AED --root_path '
          '"D:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',
          ]
'''

COMMANDS=['Python -u run.py --is_training 1 --model_id AluminumAnode --model Informer --data AED --augmentation_ratio 1 '
          '--num_sample_aug '
          '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.01 '
          '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',

          'Python -u run.py --is_training 1 --model_id AluminumAnode --model Informer --data AED --augmentation_ratio 1 '
          '--num_sample_aug '
          '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001 '
          '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',

          'Python -u run.py --is_training 1 --model_id AluminumAnode --model Informer --data AED --augmentation_ratio 1 '
          '--num_sample_aug '
          '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.0001 '
          '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',

          ]
COMMANDS1=['Python -u run.py --is_training 1 --model_id AluminumAnode --model Informer --data AED --augmentation_ratio 1 '
          '--num_sample_aug '
          '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.0001  --lradj type1 '
          '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',

          'Python -u run.py --is_training 1 --model_id AluminumAnode --model Informer --data AED --augmentation_ratio 1 '
          '--num_sample_aug '
          '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.0001  --lradj type2 '
          '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',

          'Python -u run.py --is_training 1 --model_id AluminumAnode --model Informer --data AED --augmentation_ratio 1 '
          '--num_sample_aug '
          '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.0001  --lradj type3 '
          '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',

           'Python -u run.py --is_training 1 --model_id AluminumAnode --model Informer --data AED --augmentation_ratio 1 '
           '--num_sample_aug '
           '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.0001  --lradj type3 '
           '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',
          ]
COMMANDS_Times_Net=['Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '    #样本数量增强
                    
                    '--e_layers 2 --batch_size 16 --d_model 16 --d_ff 32 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--num_sample_aug --augmentation_ratio 1 --jitter '
                    '--e_layers 2 --batch_size 16 --d_model 16 --d_ff 32 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--num_sample_aug --augmentation_ratio 1 --jitter --timewarp --scaling '
                    '--e_layers 2 --batch_size 16 --d_model 16 --d_ff 32 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    # 引入diff滤波
                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--diff_std --diff_std_multiplier 3 '
                    '--e_layers 2 --batch_size 16 --d_model 16 --d_ff 32 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--diff_std --diff_std_multiplier 5 '
                    '--e_layers 2 --batch_size 16 --d_model 16 --d_ff 32 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--diff_std --diff_std_multiplier 10 '
                    '--e_layers 2 --batch_size 16 --d_model 16 --d_ff 32 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',
                    # 引入diff滤波+样本数量扩充
                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--num_sample_aug --augmentation_ratio 1 --jitter --timewarp --scaling '
                    '--diff_std --diff_std_multiplier 3 '
                    '--e_layers 2 --batch_size 16 --d_model 16 --d_ff 32 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--num_sample_aug --augmentation_ratio 1 --jitter --timewarp --scaling '
                    '--diff_std --diff_std_multiplier 5 '
                    '--e_layers 2 --batch_size 16 --d_model 16 --d_ff 32 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--num_sample_aug --augmentation_ratio 1 --jitter --timewarp --scaling '
                    '--diff_std --diff_std_multiplier 10 '
                    '--e_layers 2 --batch_size 16 --d_model 16 --d_ff 32 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

# 样本数量增强 增大模型
                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '  

                    '--e_layers 2 --batch_size 16 --d_model 32 --d_ff 64 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--num_sample_aug --augmentation_ratio 1 --jitter '
                    '--e_layers 2 --batch_size 16 --d_model 32 --d_ff 64 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--num_sample_aug --augmentation_ratio 1 --jitter --timewarp --scaling '
                    '--e_layers 2 --batch_size 16 --d_model 32 --d_ff 64 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    # 引入diff滤波
                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--diff_std --diff_std_multiplier 3 '
                    '--e_layers 2 --batch_size 16 --d_model 32 --d_ff 64 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--diff_std --diff_std_multiplier 5 '
                    '--e_layers 2 --batch_size 16 --d_model 32 --d_ff 64 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--diff_std --diff_std_multiplier 10 '
                    '--e_layers 2 --batch_size 16 --d_model 32 --d_ff 64 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',
                    # 引入diff滤波+样本数量扩充
                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--num_sample_aug --augmentation_ratio 1 --jitter --timewarp --scaling '
                    '--diff_std --diff_std_multiplier 3 '
                    '--e_layers 2 --batch_size 16 --d_model 32 --d_ff 64 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--num_sample_aug --augmentation_ratio 1 --jitter --timewarp --scaling '
                    '--diff_std --diff_std_multiplier 5 '
                    '--e_layers 2 --batch_size 16 --d_model 32 --d_ff 64 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',

                    'Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '
                    '--num_sample_aug --augmentation_ratio 1 --jitter --timewarp --scaling '
                    '--diff_std --diff_std_multiplier 10 '
                    '--e_layers 2 --batch_size 16 --d_model 32 --d_ff 64 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',
                    ]

COMMANDS_test=['Python -u run.py --is_training 1 --model_id AluminumAnode --model TimesNet --data AED '  

                    '--e_layers 2 --batch_size 16 --d_model 32 --d_ff 64 --top_k 3 '
                    '--data AED --augmentation_ratio 2 --jitter --learning_rate 0.001  --lradj type3 '
                    '--root_path "C:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --itr 1 --train_epochs 30 --patience 10',]

if __name__ == '__main__':
    failed=0
    for cmd in COMMANDS_test:
        print('Running command: {}'.format(cmd))
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            print('Command failed: {}'.format(cmd))
            failed+=1
    if failed>0:
        print(f"\n{failed}/{len(COMMANDS)} 个命令执行失败")
        sys.exit(1)
    else:
        print("\n所有命令执行成功")