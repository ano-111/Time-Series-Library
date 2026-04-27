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
          '--data AED --augmentation_ratio 2 --jitter '
          '--root_path "D:\\Datasets\\ts-lib\\dataset\\AluminumAnode" --num_workers 0 --batch_size 32 --itr 1 --train_epochs 100 --patience 20',]
if __name__ == '__main__':
    failed=0
    for cmd in COMMANDS:
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