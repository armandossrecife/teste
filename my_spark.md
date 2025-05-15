Comando para executar uma análise distribuída em um cluster Apache Spartk

```bat
Start-Process -NoNewWindow -FilePath "docker" -ArgumentList @(
  "exec",
  "spark-master",
  "spark-submit",
  "--master spark://spark-master:7077",
  "--executor-memory 2G",
  "--driver-memory 2G",
  "--total-executor-cores 4",
  "--conf spark.executor.instances=2",
  "--conf spark.sql.shuffle.partitions=4",
  "--conf spark.driver.extraJavaOptions=`"-Dio.netty.tryReflectionSetAccessible=true`"",
  "--conf spark.executor.extraJavaOptions=`"-Dio.netty.tryReflectionSetAccessible=true`"",
  "--conf spark.serializer=org.apache.spark.serializer.KryoSerializer",
  "--conf spark.kryoserializer.buffer.max=512m",
  "/app/spark_analysis.py"
) -RedirectStandardOutput "spark-submit.log" -RedirectStandardError "spark-submit-error.log"
```
