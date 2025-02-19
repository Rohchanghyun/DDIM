import argparse

parser = argparse.ArgumentParser(description='reid')

parser.add_argument('--data_path',
                    default="/workspace/Market-1501",
                    help='path of Market-1501')

parser.add_argument(
    "--config", type=str, required=True, help="Path to the config file"
)

parser.add_argument(
        "--doc",
        type=str,
        required=True,
        help="A string for documentation purpose. "
        "Will be the name of the log folder.",
    )

parser.add_argument(
        "--exp", type=str, default="exp", help="Path for saving running related data."
    )

parser.add_argument('--mode',
                    default='train', choices=['train', 'evaluate', 'rank', 'ext', 'tsne'],
                    help='train or evaluate ')

parser.add_argument('--query_image',
                    default='0005_c6s1_004576_00.jpg',
                    help='path to the image you want to query')

parser.add_argument('--freeze',
                    default=False,
                    help='freeze backbone or not ')

parser.add_argument('--weight',
                    default='weights/model.pt',
                    help='load weights ')

parser.add_argument('--epoch',
                    default=500,
                    help='number of epoch to train')

parser.add_argument('--lr',
                    default=2e-4,
                    help='initial learning_rate')

parser.add_argument('--lr_scheduler',
                    default=[320, 380],
                    help='MultiStepLR,decay the learning rate')

parser.add_argument("--batchid",
                    default=4,
                    help='the batch for id')

parser.add_argument("--batchimage",
                    default=4,
                    help='the batch of per id')

parser.add_argument("--batchtest",
                    default=8,
                    help='the batch size for test')


opt = parser.parse_args()
