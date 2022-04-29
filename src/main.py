from diagrams import Cluster, Diagram
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.aws.ml import Sagemaker
from diagrams.aws.compute import Lambda
from diagrams.aws.mobile import APIGateway
from diagrams.aws.analytics import KinesisDataFirehose, Quicksight


with Diagram(name="example", filename="diagrams/example", curvestyle="curved"):
    with Cluster("AWS Cloud"):
        API_Gateway = APIGateway("Amazon API Gateway")
        model_and_data_bucket = SimpleStorageServiceS3("model and\n data bucket")
        results_bucket = SimpleStorageServiceS3("results bucket")

        Lambda_funtion = Lambda("AWS Lambda")
        Kinesis = KinesisDataFirehose("Amazon Kinesis\n Data Firehose")

        with Cluster("Fraud Detection"):
            xgboost = Sagemaker("xgboost")

        with Cluster("Anomaly Detection"):
            random_forest = Sagemaker("random forest")

        with Cluster("Optional"):
            QS = Quicksight("Amazon Quicksight")    

    model_and_data_bucket >> [random_forest, xgboost] << Lambda_funtion 
    [random_forest, xgboost] >> Lambda_funtion
    Lambda_funtion >> Kinesis >> results_bucket >> QS
    Lambda_funtion << API_Gateway