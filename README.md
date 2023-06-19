# lambda-create-metric-filter-pattern

Lambda script which automates creating custom metric filters which can be published to a custom cloudwatch metric, provided the below event object is provided:
```
{
  "metrics": [
    {
      "logGroupName": "/aws/lambda/Function2",
      "filterName": "Function2-ERROR-filter-metric",
      "filterPattern": "ERROR -ConcurrentRunsExceededException",
      "metricName": "Function2-ERROR-filter-metric",
      "metricNamespace": "Function2-ERROR-filter-metric",
      "metricValue": "1"
    }
  ]
}
```

OR 
```
{
    "metrics":[
     {
        "logGroupName" : " ",
        "filterName" : " ",
        "filterPattern" : " ",
        "metricName": " ",
        "metricNamespace" : " ",
        "metricValue" : " "
    },
    {
        "logGroupName" : " ",
        "filterName" : " ",
        "filterPattern" : " ",
        "metricName": " ",
        "metricNamespace" : " ",
        "metricValue" : " "
    },
    {
        "logGroupName" : " ",
        "filterName" : " ",
        "filterPattern" : " ",
        "metricName": " ",
        "metricNamespace" : " ",
        "metricValue" : " "
    }
    ]
}
```

Use-case:
1. Custom dash to get notified for specific error messages thrown.
