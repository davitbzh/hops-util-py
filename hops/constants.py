"""
String Constants used in Hops-Util: Environment variables, Kafka Config, SSL Config etc.
"""


class HTTP_CONFIG:
    """
    HTTP String constants
    """
    HTTP_CONTENT_TYPE = "Content-type"
    HTTP_APPLICATION_JSON = "application/json"
    HTTP_AUTHORIZATION = "Authorization"
    HTTP_POST = "POST"
    HTTP_PUT = "PUT"
    HTTP_GET = "GET"
    HTTP_DELETE = "DELETE"
    HTTP_UNAUTHORIZED = 401


class ENV_VARIABLES:
    """
    Environment variable names (accessible in os.environ)
    """
    KAFKA_BROKERS_ENV_VAR = "KAFKA_BROKERS"
    ELASTIC_ENDPOINT_ENV_VAR = "ELASTIC_ENDPOINT"
    PWD_ENV_VAR = "PWD"
    KAFKA_VERSION_ENV_VAR = "KAFKA_VERSION"
    LIVY_VERSION_ENV_VAR = "LIVY_VERSION"
    SPARK_VERSION_ENV_VAR = "SPARK_VERSION"
    REST_ENDPOINT_END_VAR = "REST_ENDPOINT"
    TENSORFLOW_VERSION_ENV_VAR = "TENSORFLOW_VERSION"
    CUDA_VERSION_ENV_VAR = "CUDA_VERSION"
    HOPSWORKS_VERSION_ENV_VAR = "HOPSWORKS_VERSION"
    HADOOP_VERSION_ENV_VAR = "HADOOP_VERSION"
    HADOOP_USER_NAME_ENV_VAR = "HADOOP_USER_NAME"
    HADOOP_HOME = "HADOOP_HOME"
    HADOOP_CLASSPATH_GLOB = "HADOOP_CLASSPATH_GLOB"
    HDFS_USER_ENV_VAR = "HDFS_USER"
    HOPSWORKS_USER_ENV_VAR = "HOPSWORKS_USER"
    PATH_ENV_VAR = "PATH"
    PYTHONPATH_ENV_VAR = "PYTHONPATH"
    JOB_NAME_ENV_VAR = "HOPSWORKS_JOB_NAME"
    KERNEL_ID_ENV_VAR = "HOPSWORKS_KERNEL_ID"
    HOPSWORKS_PROJECT_ID_ENV_VAR = "HOPSWORKS_PROJECT_ID"
    HOPSWORKS_PROJECT_NAME_ENV_VAR = "HOPSWORKS_PROJECT_NAME"
    API_KEY_ENV_VAR = "API_KEY"
    REGION_NAME_ENV_VAR = "REGION_NAME"
    FLINK_CONF_DIR = "FLINK_CONF_DIR"
    FLINK_LIB_DIR = "FLINK_LIB_DIR"
    REQUESTS_VERIFY = "REQUESTS_VERIFY"
    REQUESTS_VERIFY_ENV_VAR = "REQUESTS_VERIFY"
    DOMAIN_CA_TRUSTSTORE_ENV_VAR = "DOMAIN_CA_TRUSTSTORE"
    DOMAIN_CA_TRUSTSTORE_PEM_ENV_VAR = "DOMAIN_CA_TRUSTSTORE_PEM"
    SECRETS_DIR_ENV_VAR = "SECRETS_DIR"


class KAFKA_SSL_CONFIG:
    """
    Kafka SSL constant strings for configuration
    """
    SSL = "SSL"
    SSL_TRUSTSTORE_LOCATION_CONFIG = "ssl.truststore.location"
    SSL_TRUSTSTORE_LOCATION_DOC = "The location of the trust store file. "
    SSL_TRUSTSTORE_PASSWORD_CONFIG = "ssl.truststore.password"
    SSL_TRUSTSTORE_PASSWORD_DOC = "The password for the trust store file. If a password is not set access to the truststore is still available, but integrity checking is disabled."
    SSL_KEYSTORE_LOCATION_CONFIG = "ssl.keystore.location"
    SSL_KEYSTORE_PASSWORD_CONFIG = "ssl.keystore.password"
    SSL_KEY_PASSWORD_CONFIG = "ssl.key.password"
    SECURITY_PROTOCOL_CONFIG = "security.protocol"
    SSL_CERTIFICATE_LOCATION_CONFIG = "ssl.certificate.location"
    SSL_CA_LOCATION_CONFIG = "ssl.ca.location"
    SSL_PRIVATE_KEY_LOCATION_CONFIG = "ssl.key.location"
    SSL_ENDPOINT_IDENTIFICATION_ALGORITHM_CONFIG = "ssl.endpoint.identification.algorithm"


# General SSL config properties

class SSL_CONFIG:
    """
    General SSL configuration constants for Hops-TLS
    """
    KEYSTORE_SUFFIX = "__kstore.jks"
    TRUSTSTORE_SUFFIX = "__tstore.jks"
    PASSWORD_SUFFIX = "__cert.key"

    K_CERTIFICATE_CONFIG = "k_certificate"
    T_CERTIFICATE_CONFIG = "t_certificate"
    PEM_CLIENT_CERTIFICATE_CONFIG = "client.pem"
    PEM_CLIENT_KEY_CONFIG = "client_key.pem"
    PEM_CA_CHAIN_CERTIFICATE_CONFIG = "ca_chain.pem"
    DOMAIN_CA_TRUSTSTORE = "domain_ca_truststore"
    CRYPTO_MATERIAL_PASSWORD = "material_passwd"
    PEM_CA_ROOT_CERT = "/srv/hops/kagent/host-certs/hops_root_ca.pem"
    SSL_ENABLED = "ipc.server.ssl.enabled"


class KAFKA_PRODUCER_CONFIG:
    """
    Constant strings for Kafka producers
    """
    BOOTSTRAP_SERVERS_CONFIG = "bootstrap.servers"
    KEY_SERIALIZER_CLASS_CONFIG = "key.serializer"
    VALUE_SERIALIZER_CLASS_CONFIG = "value.serializer"


class KAFKA_CONSUMER_CONFIG:
    """
    Constant strings for Kafka consumers
    """
    GROUP_ID_CONFIG = "group.id"
    ENABLE_AUTO_COMMIT_CONFIG = "enable.auto.commit"
    AUTO_COMMIT_INTERVAL_MS_CONFIG = "auto.commit.interval.ms"
    SESSION_TIMEOUT_MS_CONFIG = "session.timeout.ms"
    KEY_DESERIALIZER_CLASS_CONFIG = "key.deserializer"
    VALUE_DESERIALIZER_CLASS_CONFIG = "value.deserializer"
    AUTO_OFFSET_RESET_CONFIG = "auto.offset.reset"
    ENABLE_AUTO_COMMIT_CONFIG = "enable.auto.commit"
    KEY_DESERIALIZER_CLASS_CONFIG = "key.deserializer"
    VALUE_DESERIALIZER_CLASS_CONFIG = "value.deserializer"


class SPARK_CONFIG:
    """
    Spark string constants
    """
    SPARK_SCHEMA_FIELD_METADATA = "metadata"
    SPARK_SCHEMA_FIELDS = "fields"
    SPARK_SCHEMA_FIELD_NAME = "name"
    SPARK_SCHEMA_FIELD_TYPE = "type"
    SPARK_SCHEMA_ELEMENT_TYPE = "elementType"
    SPARK_OVERWRITE_MODE = "overwrite"
    SPARK_APPEND_MODE = "append"
    SPARK_WRITE_DELIMITER = "delimiter"
    SPARK_INFER_SCHEMA = "inferSchema"
    SPARK_WRITE_HEADER = "header"
    SPARK_TF_CONNECTOR_RECORD_TYPE = "recordType"
    SPARK_TF_CONNECTOR_RECORD_TYPE_EXAMPLE = "Example"
    SPARK_LONG_TYPE = "long"
    SPARK_SHORT_TYPE = "short"
    SPARK_BYTE_TYPE = "byte"
    SPARK_INTEGER_TYPE = "integer"
    SPARK_INT_TYPE = "int"
    SPARK_FLOAT_TYPE = "float"
    SPARK_DOUBLE_TYPE = 'double'
    SPARK_DECIMAL_TYPE = "decimal"
    SPARK_BIGINT_TYPE = "bigint"
    SPARK_SMALLINT_TYPE = "smallint"
    SPARK_STRING_TYPE = "string"
    SPARK_BINARY_TYPE = "binary"
    SPARK_NUMERIC_TYPES = [SPARK_BIGINT_TYPE,
                           SPARK_DECIMAL_TYPE,
                           SPARK_INTEGER_TYPE,
                           SPARK_INT_TYPE,
                           SPARK_DOUBLE_TYPE,
                           SPARK_LONG_TYPE,
                           SPARK_FLOAT_TYPE,
                           SPARK_SHORT_TYPE]
    SPARK_STRUCT = "struct"
    SPARK_ARRAY = "array"
    SPARK_ARRAY_DOUBLE = "array<double>"
    SPARK_ARRAY_INTEGER = "array<integer>"
    SPARK_ARRAY_INT = "array<int>"
    SPARK_ARRAY_BIGINT = "array<bigint>"
    SPARK_ARRAY_FLOAT = "array<float>"
    SPARK_ARRAY_DECIMAL = "array<decimal>"
    SPARK_ARRAY_STRING = "array<string>"
    SPARK_ARRAY_LONG = "array<long>"
    SPARK_ARRAY_BINARY = "array<binary>"
    SPARK_VECTOR = "vector"
    SPARK_SQL_CATALOG_IMPLEMENTATION = "spark.sql.catalogImplementation"
    SPARK_SQL_CATALOG_HIVE = "hive"
    SPARK_JDBC_FORMAT= "jdbc"
    SPARK_JDBC_URL= "url"
    SPARK_JDBC_DBTABLE= "dbtable"
    SPARK_JDBC_USER = "user"
    SPARK_JDBC_PW = "password"

class MODEL_SERVING:
    MODELS_DATASET = "Models"
    SERVING_TYPE_TENSORFLOW = "TENSORFLOW"
    SERVING_TYPE_SKLEARN = "SKLEARN"
    SERVING_TYPES = [SERVING_TYPE_TENSORFLOW, SERVING_TYPE_SKLEARN]
    SERVING_ACTION_START = "START"
    SERVING_ACTION_STOP = "STOP"
    SERVING_ACTIONS = [SERVING_ACTION_STOP, SERVING_ACTION_STOP]
    SERVING_START_OR_STOP_PATH_PARAM = "?action="

class FEATURE_STORE:
    """
     Featurestore constants
    """
    TRAINING_DATASET_PROVENANCE_FEATUREGROUP = "featuregroup"
    TRAINING_DATASET_PROVENANCE_VERSION = "version"
    MAX_CORRELATION_MATRIX_COLUMNS = 50
    TRAINING_DATASET_CSV_FORMAT = "csv"
    TRAINING_DATASET_TSV_FORMAT = "tsv"
    TRAINING_DATASET_PARQUET_FORMAT = "parquet"
    TRAINING_DATASET_TFRECORDS_FORMAT = "tfrecords"
    TRAINING_DATASET_TFRECORD_FORMAT = "tfrecord"
    TRAINING_DATASET_AVRO_FORMAT = "avro"
    TRAINING_DATASET_ORC_FORMAT = "orc"
    TRAINING_DATASET_NPY_FORMAT = "npy"
    TRAINING_DATASET_IMAGE_FORMAT = "image"
    TRAINING_DATASET_HDF5_FORMAT = "hdf5"
    TRAINING_DATASET_PETASTORM_FORMAT = "petastorm"
    TRAINING_DATASET_NPY_SUFFIX = ".npy"
    TRAINING_DATASET_HDF5_SUFFIX = ".hdf5"
    TRAINING_DATASET_CSV_SUFFIX = ".csv"
    TRAINING_DATASET_TSV_SUFFIX = ".tsv"
    TRAINING_DATASET_PARQUET_SUFFIX = ".parquet"
    TRAINING_DATASET_AVRO_SUFFIX = ".avro"
    TRAINING_DATASET_ORC_SUFFIX = ".orc"
    TRAINING_DATASET_IMAGE_SUFFIX = ".image"
    TRAINING_DATASET_TFRECORDS_SUFFIX = ".tfrecords"
    TRAINING_DATASET_PETASTORM_SUFFIX = ".petastorm"
    TRAINING_DATASET_SUPPORTED_FORMATS = [
        TRAINING_DATASET_TSV_FORMAT,
        TRAINING_DATASET_CSV_FORMAT,
        TRAINING_DATASET_PARQUET_FORMAT,
        TRAINING_DATASET_TFRECORDS_FORMAT,
        TRAINING_DATASET_TFRECORD_FORMAT,
        TRAINING_DATASET_NPY_FORMAT,
        TRAINING_DATASET_HDF5_FORMAT,
        TRAINING_DATASET_AVRO_FORMAT,
        TRAINING_DATASET_ORC_FORMAT,
        TRAINING_DATASET_IMAGE_FORMAT,
        TRAINING_DATASET_PETASTORM_FORMAT
    ]
    FEATURE_GROUP_INSERT_APPEND_MODE = "append"
    FEATURE_GROUP_INSERT_OVERWRITE_MODE = "overwrite"
    FEATURESTORE_SUFFIX =  "_featurestore"
    TRAINING_DATASETS_SUFFIX =  "_Training_Datasets"
    TRAINING_DATASET_TF_RECORD_SCHEMA_FILE_NAME = "tf_record_schema.txt"
    TF_RECORD_SCHEMA_FEATURE = "feature"
    TF_RECORD_SCHEMA_FEATURE_FIXED = "fixed_len"
    TF_RECORD_SCHEMA_FEATURE_VAR = "var_len"
    TF_RECORD_SCHEMA_TYPE = "type"
    TF_RECORD_SCHEMA_SHAPE = "shape"
    TF_RECORD_INT_TYPE = "int"
    TF_RECORD_FLOAT_TYPE = "float"
    TF_RECORD_STRING_TYPE = "string"
    TF_RECORD_INT_ARRAY_SPARK_TYPES = [SPARK_CONFIG.SPARK_ARRAY_INTEGER, SPARK_CONFIG.SPARK_ARRAY_BIGINT,
                                       SPARK_CONFIG.SPARK_ARRAY_INT, SPARK_CONFIG.SPARK_ARRAY_LONG]
    TF_RECORD_INT_SPARK_TYPES = [SPARK_CONFIG.SPARK_INTEGER_TYPE, SPARK_CONFIG.SPARK_BIGINT_TYPE,
                                 SPARK_CONFIG.SPARK_INT_TYPE, SPARK_CONFIG.SPARK_LONG_TYPE]
    TF_RECORD_STRING_SPARK_TYPES = [SPARK_CONFIG.SPARK_STRING_TYPE, SPARK_CONFIG.SPARK_BINARY_TYPE]
    TF_RECORD_STRING_ARRAY_SPARK_TYPES = [SPARK_CONFIG.SPARK_ARRAY_STRING, SPARK_CONFIG.SPARK_ARRAY_BINARY]
    TF_RECORD_FLOAT_SPARK_TYPES = [SPARK_CONFIG.SPARK_FLOAT_TYPE, SPARK_CONFIG.SPARK_DECIMAL_TYPE,
                                   SPARK_CONFIG.SPARK_DOUBLE_TYPE]
    TF_RECORD_FLOAT_ARRAY_SPARK_TYPES = [SPARK_CONFIG.SPARK_ARRAY_FLOAT, SPARK_CONFIG.SPARK_ARRAY_DECIMAL,
                                   SPARK_CONFIG.SPARK_ARRAY_DOUBLE, SPARK_CONFIG.SPARK_VECTOR]
    RECOGNIZED_TF_RECORD_TYPES = [SPARK_CONFIG.SPARK_VECTOR, SPARK_CONFIG.SPARK_ARRAY_BINARY,
                                  SPARK_CONFIG.SPARK_ARRAY_STRING, SPARK_CONFIG.SPARK_ARRAY_DECIMAL,
                                  SPARK_CONFIG.SPARK_ARRAY_DOUBLE, SPARK_CONFIG.SPARK_ARRAY_FLOAT,
                                  SPARK_CONFIG.SPARK_ARRAY_LONG, SPARK_CONFIG.SPARK_ARRAY_INTEGER,
                                  SPARK_CONFIG.SPARK_BINARY_TYPE, SPARK_CONFIG.SPARK_STRING_TYPE,
                                  SPARK_CONFIG.SPARK_DECIMAL_TYPE, SPARK_CONFIG.SPARK_DOUBLE_TYPE,
                                  SPARK_CONFIG.SPARK_FLOAT_TYPE, SPARK_CONFIG.SPARK_LONG_TYPE,
                                  SPARK_CONFIG.SPARK_INT_TYPE, SPARK_CONFIG.SPARK_INTEGER_TYPE,
                                  SPARK_CONFIG.SPARK_ARRAY_BIGINT, SPARK_CONFIG.SPARK_BIGINT_TYPE,
                                  SPARK_CONFIG.SPARK_ARRAY_INT
                                  ]
    DATAFRAME_TYPE_SPARK = "spark"
    DATAFRAME_TYPE_NUMPY = "numpy"
    DATAFRAME_TYPE_PYTHON = "python"
    DATAFRAME_TYPE_PANDAS = "pandas"
    JDBC_TRUSTSTORE_ARG = "sslTrustStore"
    JDBC_TRUSTSTORE_PW_ARG = "trustStorePassword"
    JDBC_KEYSTORE_ARG = "sslKeyStore"
    JDBC_KEYSTORE_PW_ARG = "keyStorePassword"
    IMPORT_HOPS_UTIL_FEATURESTORE_HELPER = "import io.hops.util.featurestore.FeaturestoreHelper"


class PETASTORM_CONFIG:
    """
    Petastorm String constants
    """
    FILESYSTEM_FACTORY = "pyarrow_filesystem"
    SCHEMA = "schema"
    LIBHDFS = "libhdfs"

class MYSQL_CONFIG:
    """ MYSQL string constants """
    MYSQL_DATA_TYPES = [
        "None", "INT(11)", "TINYINT(1)", "SMALLINT(5)", "MEDIUMINT(7)", "BIGINT(20)", "FLOAT", "DOUBLE", "DECIMAL",
        "DATE", "DATETIME", "TIMESTAMP", "TIME", "YEAR", "CHAR", "VARCHAR(25)", "VARCHAR(125)", "VARCHAR(225)",
        "VARCHAR(500)", "VARCHAR(1000)", "VARCHAR(2000)", "VARCHAR(5000)", "VARCHAR(10000)", "BLOB", "TEXT",
        "TINYBLOB", "TINYTEXT", "MEDIUMBLOB", "MEDIUMTEXT", "LONGBLOB", "LONGTEXT", "JSON"
    ]
    MYSQL_BIGINT_TYPE = "BIGINT(20)"
    MYSQL_SMALLINT_TYPE = "SMALLINT(5)"
    MYSQL_CHAR_TYPE = "CHAR"
    MYSQL_INTEGER_TYPE = "INT(11)"
    MYSQL_VARCHAR_1000_TYPE = "VARCHAR(1000)"
    MYSQL_BLOB_TYPE = "BLOB"

class HIVE_CONFIG:
    """
    Hive string constants
    """
    HIVE_DATA_TYPES = [
        "TINYINT", "SMALLINT", "INT", "BIGINT", "FLOAT", "DOUBLE",
        "DECIMAL", "TIMESTAMP", "DATE", "INTERVAL", "STRING", "VARCHAR",
        "CHAR", "BOOLEAN", "BINARY", "ARRAY", "MAP", "STRUCT", "UNIONTYPE"
    ]
    HIVE_BIGINT_TYPE = "BIGINT"
    HIVE_INT_TYPE = "INT"
    HIVE_CHAR_TYPE = "CHAR"


class REST_CONFIG:
    """
    REST endpoints and JSON properties used for communicating with Hopsworks REST API
    """
    JSON_KEYSTOREPWD = "keyStorePwd"
    JSON_SCHEMA_CONTENTS = "contents"

    JSON_TYPE="type"

    JSON_FEATURESTORE_UPDATE_STATS_QUERY_PARAM = "updateStats"
    JSON_FEATURESTORE_UPDATE_METADATA_QUERY_PARAM = "updateMetadata"
    JSON_FEATURESTORE_UPDATE_JOB_QUERY_PARAM = "updateJob"
    JSON_FEATURESTORE_ENABLE_ONLINE_QUERY_PARAM = "enableOnline"
    JSON_FEATURESTORE_DISABLE_ONLINE_QUERY_PARAM = "disableOnline"
    JSON_FEATURESTORE_UPDATE_STATISTICS_SETTINGS = "updateStatsSettings"
    JSON_FEATURESTORE_SETTINGS_ENTITY_NAME_MAX_LENGTH = "featurestoreEntityNameMaxLength"
    JSON_FEATURESTORE_SETTINGS_ENTITY_DESCRIPTION_MAX_LENGTH = "featurestoreEntityDescriptionMaxLength"
    JSON_FEATURESTORE_SETTINGS_CACHED_FEATUREGROUP_DTO_TYPE = "cachedFeaturegroupDtoType"
    JSON_FEATURESTORE_SETTINGS_EXTERNAL_TRAINING_DATASET_TYPE = "externalTrainingDatasetType"
    JSON_FEATURESTORE_SETTINGS_FEATURESTORE_REGEX = "featurestoreRegex"
    JSON_FEATURESTORE_SETTINGS_HOPSFS_CONNECTOR_DTO_TYPE = "hopsfsConnectorDtoType"
    JSON_FEATURESTORE_SETTINGS_HOPSFS_CONNECTOR_TYPE = "hopsfsConnectorType"
    JSON_FEATURESTORE_SETTINGS_HOPSFS_TRAINING_DATASET_TYPE = "hopsfsTrainingDatasetType"
    JSON_FEATURESTORE_SETTINGS_JDBC_CONNECTOR_DTO_TYPE = "jdbcConnectorDtoType"
    JSON_FEATURESTORE_SETTINGS_JDBC_CONNECTOR_TYPE = "jdbcConnectorType"
    JSON_FEATURESTORE_SETTINGS_JDBC_CONNECTOR_ARGUMENTS_MAX_LEN = "jdbcStorageConnectorArgumentsMaxLength"
    JSON_FEATURESTORE_SETTINGS_JDBC_CONNECTOR_CONNECTION_STRING_MAX_LEN = \
        "jdbcStorageConnectorConnectionstringMaxLength"
    JSON_FEATURESTORE_SETTINGS_ON_DEMAND_FEATUREGROUP_DTO_TYPE = "onDemandFeaturegroupDtoType"
    JSON_FEATURESTORE_SETTINGS_ON_DEMAND_FEATUREGROUP_SQL_QUERY_MAX_LEN = "onDemandFeaturegroupSqlQueryMaxLength"
    JSON_FEATURESTORE_SETTINGS_S3_CONNECTOR_DTO_TYPE = "s3ConnectorDtoType"
    JSON_FEATURESTORE_SETTINGS_S3_CONNECTOR_TYPE = "s3ConnectorType"
    JSON_FEATURESTORE_SETTINGS_S3_CONNECTOR_ACCESS_KEY_MAX_LEN = "s3StorageConnectorAccesskeyMaxLength"
    JSON_FEATURESTORE_SETTINGS_S3_CONNECTOR_BUCKET_MAX_LEN = "s3StorageConnectorBucketMaxLength"
    JSON_FEATURESTORE_SETTINGS_S3_CONNECTOR_SECRET_KEY_MAX_LEN = "s3StorageConnectorSecretkeyMaxLength"
    JSON_FEATURESTORE_SETTINGS_STORAGE_CONNECTOR_DESCRIPTION_MAX_LEN = "storageConnectorDescriptionMaxLength"
    JSON_FEATURESTORE_SETTINGS_STORAGE_CONNECTOR_NAME_MAX_LEN = "storageConnectorDescriptionMaxLength"
    JSON_FEATURESTORE_SETTINGS_HIVE_SUGGESTED_FEATURE_TYPES = "suggestedHiveFeatureTypes"
    JSON_FEATURESTORE_SETTINGS_MYSQL_SUGGESTED_FEATURE_TYPES = "suggestedMysqlFeatureTypes"
    JSON_FEATURESTORE_SETTINGS_TRAINING_DATASET_DATA_FORMATS = "trainingDatasetDataFormats"
    JSON_FEATURESTORE_SETTINGS_TRAINING_DATASET_TYPE = "trainingDatasetType"
    JSON_FEATURESTORE_SETTINGS = "settings"
    JSON_FEATURESTORE_STORAGE_CONNECTORS = "storageConnectors"
    JSON_FEATURESTORE_SETTINGS_IMPORT_CONNECTORS = "featureImportConnectors"
    JSON_FEATURESTORE_SETTINGS_ONLINE_ENABLED = "onlineFeaturestoreEnabled"

    JSON_FEATURESTORE_JOB_FEATUREGROUP_ID = "featuregroupId"
    JSON_FEATURESTORE_JOB_TRAINING_DATASET_ID = "trainingDatasetId"
    JSON_FEATURESTORE_JOB_LAST_COMPUTED = "lastComputed"
    JSON_FEATURESTORE_JOB_STATUS = "jobStatus"
    JSON_FEATURESTORE_JOB_NAME = "jobName"
    JSON_FEATURESTORE_JOB_ID = "jobId"
    JSON_FEATURESTORE_LOCATION = "location"

    JSON_FEATUREGROUP_ON_DEMAND_QUERY = "query"
    JSON_FEATUREGROUP_JDBC_CONNECTOR_NAME = "jdbcConnectorName"
    JSON_FEATUREGROUP_JDBC_CONNECTOR_ID = "jdbcConnectorId"
    JSON_FEATUREGROUP_TYPE = "type"
    JSON_FEATUREGROUP_NAME = "name"
    JSON_FEATUREGROUP_ID = "id"
    JSON_FEATUREGROUP_VERSION = "version"
    JSON_FEATUREGROUP_JOBS = "jobs"
    JSON_FEATUREGROUP_FEATURES = "features"
    JSON_FEATUREGROUP_DESCRIPTION = "description"
    JSON_FEATUREGROUP_CREATED = "created"
    JSON_FEATUREGROUP_CREATOR = "creator"
    JSON_FEATUREGROUPS = "featuregroups"
    JSON_FEATUREGROUP_ONLINE = "onlineEnabled"
    JSON_FEATUREGROUP_HUDI = "hudiEnabled"
    JSON_FEATUREGROUP_FEATURE_HISTOGRAM_ENABLED = "featHistEnabled"
    JSON_FEATUREGROUP_FEATURE_CORRELATION_ENABLED = "featCorrEnabled"
    JSON_FEATUREGROUP_DESCRIPTIVE_STATISTICS_ENABLED = "descStatsEnabled"
    JSON_FEATUREGROUP_STATISTIC_COLUMNS = "statisticColumns"
    JSON_FEATUREGROUP_TIME_TRAVEL_FORMAT = "time_travel_format"

    JSON_ONLINE_FEATUREGROUP_ID = "id"
    JSON_ONLINE_FEATUREGROUP_DB = "dbName"
    JSON_ONLINE_FEATUREGROUP_TABLE = "tableName"
    JSON_ONLINE_FEATUREGROUP_TABLE_TYPE = "tableType"
    JSON_ONLINE_FEATUREGROUP_TABLE_ROWS = "tableRows"
    JSON_ONLINE_FEATUREGROUP_SIZE = "size"


    JSON_FEATURESTORE = "featurestore"
    JSON_FEATURESTORE_ID = "featurestoreId"
    JSON_FEATURESTORE_NAME = "featurestoreName"
    JSON_FEATURESTORE_PROJECT_ID = "projectId"
    JSON_FEATURESTORE_PROJECT_NAME = "projectName"
    JSON_FEATURESTORE_INODE_ID = "inodeId"
    JSON_FEATURESTORE_DESCRIPTION = "featurestoreDescription"
    JSON_FEATURESTORE_HDFS_PATH = "hdfsStorePath"
    JSON_FEATURESTORE_ONLINE_CONNECTOR = "onlineFeaturestoreConnector"
    JSON_FEATURESTORE_ONLINE_ENABLED = "onlineEnabled"
    JSON_FEATURESTORE_ONLINE_FEATURESTORE_TYPE = "onlineFeaturestoreType"
    JSON_FEATURESTORE_OFFLINE_FEATURESTORE_TYPE = "offlineFeaturestoreType"
    JSON_FEATURESTORE_ONLINE_FEATURESTORE_NAME = "onlineFeaturestoreName"
    JSON_FEATURESTORE_OFFLINE_FEATURESTORE_NAME = "offlineFeaturestoreName"

    JSON_FEATURE_NAME = "name"
    JSON_FEATURE_TYPE = "type"
    JSON_FEATURE_INDEX = "index"
    JSON_FEATURE_DESCRIPTION = "description"
    JSON_FEATURE_PRIMARY = "primary"
    JSON_FEATURE_PARTITION = "partition"
    JSON_FEATURE_ONLINE_TYPE = "onlineType"
    JSON_FEATURE_FEATUREGROUP = "featuregroup"
    JSON_FEATURE_VERSION = "version"

    JSON_TRAINING_DATASET_EXTERNAL_TYPE = "EXTERNAL_TRAINING_DATASET"
    JSON_TRAINING_DATASET_HOPSFS_TYPE = "HOPSFS_TRAINING_DATASET"
    JSON_TRAINING_DATASET_TYPE = "trainingDatasetType"
    JSON_TRAINING_DATASET_CONNECTOR_NAME = "storageConnectorName"
    JSON_TRAINING_DATASET_CONNECTOR_ID = "storageConnectorId"
    JSON_TRAINING_DATASET_SIZE = "size"
    JSON_TRAINING_DATASET_ID = "id"
    JSON_TRAINING_DATASET_NAME = "name"
    JSON_TRAINING_DATASETS = "trainingDatasets"
    JSON_TRAINING_DATASET_HDFS_STORE_PATH = "hdfsStorePath"
    JSON_TRAINING_DATASET_FORMAT = "dataFormat"
    JSON_TRAINING_DATASET_SCHEMA = "features"
    JSON_TRAINING_DATASET_VERSION = "version"
    JSON_TRAINING_DATASET_CREATOR = "creator"
    JSON_TRAINING_DATASET_CREATED = "created"
    JSON_TRAINING_DATASET_DESCRIPTION = "description"
    JSON_TRAINING_DATASET_JOBNAME = "jobName"
    JSON_TRAINING_DATASET_INODE_ID = "inodeId"
    JSON_TRAINING_DATASET_FEATURES = "features"
    JSON_TRAINING_DATASET_JOBS = "jobs"

    JSON_FEATURESTORE_HOPSFS_CONNECTOR_HOPSFS_PATH = "hopsfsPath"
    JSON_FEATURESTORE_HOPSFS_CONNECTOR_DATASET_NAME = "datasetName"

    JSON_FEATURESTORE_JDBC_CONNECTOR_CONNECTION_STRING = "connectionString"
    JSON_FEATURESTORE_JDBC_CONNECTOR_ARGUMENTS = "arguments"

    JSON_FEATURESTORE_S3_ACCESS_KEY = "accessKey"
    JSON_FEATURESTORE_S3_SECRET_KEY = "secretKey"
    JSON_FEATURESTORE_S3_BUCKET = "bucket"

    JSON_FEATURESTORE_CONNECTOR_NAME = "name"
    JSON_FEATURESTORE_CONNECTOR_DESCRIPTION = "description"
    JSON_FEATURESTORE_CONNECTOR_ID = "id"
    JSON_FEATURESTORE_CONNECTOR_FEATURESTORE_ID = "featurestoreId"
    JSON_FEATURESTORE_CONNECTOR_TYPE = "storageConnectorType"

    JSON_SCHEMA_VERSION = "version"
    JSON_KEYSTORE = "keyStore"

    HOPSWORKS_REST_RESOURCE = "hopsworks-api/api"
    HOPSWORKS_SCHEMA_RESOURCE = "schema"
    HOPSWORKS_FEATURESTORES_RESOURCE = "featurestores"
    HOPSWORKS_FEATURESTORE_METADATA_RESOURCE = "metadata"
    HOPSWORKS_FEATUREGROUPS_RESOURCE = "featuregroups"
    HOPSWORKS_TRAININGDATASETS_RESOURCE = "trainingdatasets"
    HOPSWORKS_FEATUREGROUP_CLEAR_RESOURCE = "clear"
    HOPSWORKS_FEATUREGROUPS_SYNC_RESOURCE = "sync"
    HOPSWORKS_SERVING_RESOURCE = "serving"
    HOPSWORKS_INFERENCE_RESOURCE = "inference"
    HOPSWORKS_MODELS_RESOURCE = "models"
    HOPSWORKS_USERS_RESOURCE = "users"
    HOPSWORKS_ADMIN_RESOURCE = "admin"
    HOPSWORKS_FEATURESTORES_STORAGE_CONNECTORS_RESOURCE = "storageconnectors"
    HOPSWORKS_ONLINE_FEATURESTORE_STORAGE_CONNECTOR_RESOURCE= "onlinefeaturestore"
    HOPSWORKS_FEATURESTORE_TAGS_RESOURCE = "tags"
    HOPSWORKS_VARIABLES_RESOURCE = "variables"
    HOPSWORKS_ENDPOINT = "hopsworks_endpoint"

    HOPSWORKS_EXPERIMENTS_RESOURCE = "experiments"

    HOPSWORKS_KAFKA_RESOURCE = "kafka"
    HOPSWORKS_TOPICS_RESOURCE = "topics"
    HOPSWORKS_SUBJECTS_RESOURCE = "subjects"

    HOPSWORKS_PROJECT_RESOURCE = "project"
    HOPSWORKS_PROJECT_INFO_RESOURCE = "getProjectInfo"
    HOPSWORKS_JOBS_RESOURCE = "jobs"
    HOPSWORKS_EXECUTIONS_RESOURCE = "executions"
    HOPSWORKS_DATASETS_RESOURCE = "dataset"
    HOPSWORKS_PROJECT_CREDENTIALS_RESOURCE = "credentials"
    HOPSWORKS_PROJECT_CLIENT = "client"
    HOPSWORKS_AUTH_RESOURCE = "auth"
    HOPSWORKS_AUTH_RESOURCE_REGISTER = "register"

    HOPSWORKS_XATTR_RESOURCE = "xattrs"
    HOPSWORKS_ELASTIC_RESOURCE = "elastic"
    HOPSWORKS_ELASTIC_JWT_RESOURCE = "jwt"

    JSON_ERROR_CODE = "errorCode"
    JSON_ERROR_MSG = "errorMsg"
    JSON_USR_MSG = "usrMsg"

    JWT_TOKEN = "token.jwt"

    JSON_SERVING_STATUS = "status"
    JSON_SERVING_ARTIFACT_PATH = "artifactPath"
    JSON_SERVING_NAME = "name"
    JSON_SERVING_CREATOR = "creator"
    JSON_SERVING_TYPE = "servingType"
    JSON_SERVING_MODEL_VERSION = "modelVersion"
    JSON_SERVING_CREATED = "created"
    JSON_SERVING_REQUESTED_INSTANCES = "requestedInstances"
    JSON_SERVING_BATCHING_ENABLED = "batchingEnabled"
    JSON_SERVING_AVAILABLE_INSTANCES = "availableInstances"
    JSON_SERVING_KAFKA_TOPIC_DTO = "kafkaTopicDTO"
    JSON_SERVING_ID = "id"
    JSON_SERVING_CREATE_KAFKA_TOPIC = "CREATE"
    JSON_SERVING_DONT_CREATE_KAFKA_TOPIC = "NONE"

    JSON_KAFKA_TOPIC_SCHEMA_VERSION = "schemaVersion"
    JSON_KAFKA_TOPIC_NAME = "name"
    JSON_KAFKA_NUM_PARTITIONS = "numOfPartitions"
    JSON_KAFKA_NUM_REPLICAS = "numOfReplicas"


class DELIMITERS:
    """
    String delimiters constants
    """
    SLASH_DELIMITER = "/"
    COMMA_DELIMITER = ","
    TAB_DELIMITER = "\t"
    COLON_DELIMITER = ":"
    DOT_DELIMITER = "."
    AMPERSAND_DELIMITER = "&"
    SEMI_COLON_DELIMITER = ";"
    JDBC_CONNECTION_STRING_VALUE_DELIMITER = "="
    JDBC_CONNECTION_STRING_DELIMITER = ";"
    QUESTION_MARK_DELIMITER = "?"


class S3_CONFIG:
    """
    String constants for S3
    """
    S3_FILE_PREFIX = "s3a://"
    S3_ACCESS_KEY_ENV = "fs.s3a.access.key"
    S3_SECRET_KEY_ENV = "fs.s3a.secret.key"
    S3_TRAINING_DATASETS_FOLDER = "TRAINING_DATASETS"

class AWS:
    DEFAULT_REGION = 'default'
    SECRETS_MANAGER = "secretsmanager"
    PARAMETER_STORE = "parameterstore"

class LOCAL:
    LOCAL_STORE = "local"

class XATTRS:
    XATTRS_PARAM_NAME = 'name'

class ELASTICSEARCH_CONFIG:
    SSL_CONFIG = "es.net.ssl"
    NODES_WAN_ONLY = "es.nodes.wan.only"
    NODES = "es.nodes"
    SSL_KEYSTORE_LOCATION = "es.net.ssl.keystore.location"
    SSL_KEYSTORE_PASSWORD = "es.net.ssl.keystore.pass"
    SSL_TRUSTSTORE_LOCATION = "es.net.ssl.truststore.location"
    SSL_TRUSTSTORE_PASSWORD = "es.net.ssl.truststore.pass"
    HTTP_AUTHORIZATION = "es.net.http.header.Authorization"
    INDEX = "es.resource"