def MyTransform (glueContext, dfc) -> DynamicFrameCollection:
    
    from awsglue.transforms import Relationalize
    from pyspark.sql import functions as sf
    from pyspark.sql.functions import lit
    
    newdfc= SelectFromCollection.apply(
    dfc=dfc,
    key=list(dfc.keys())[0],
    transformation_ctx="newdfc",
    )
    
    glue_temp_storage = "s3://aws-glue-assets-321179548224-us-east-1/temporary/"
    dfc_root_table_name = "root"
    
    ApplyMapping_node3 = Relationalize.apply(
    frame=newdfc,
    staging_path=glue_temp_storage,
        name=dfc_root_table_name,
    transformation_ctx="ApplyMapping_node3",
    )
    
    data = ApplyMapping_node3.select(dfc_root_table_name)
    
    #rename column
    # error : DynamicFrame has no attribute withColumnRenamed
    # data = data.withColumnRenamed('properties.page.title:string','product') 
    
    # add label
    data = data.withColumn("~label", lit('customer_behavior'))
    # create id
    data = data.withColumn('~id', sf.hash("properties.page.title:string"))    
    
    return (DynamicFrameCollection({"CustomTransform0": data}, glueContext))
    
    
    
    
    
    
    