```python
pd.DataFrame(index=c["billno"].tolist(),data=c["json_data"].map(lambda x:json.loads(x)).tolist())
```

