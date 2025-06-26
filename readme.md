# POC digital twin
Playground for digital Twin Concept.

this project is a simulating function.
it makes models from from data (csv) with ML
you adjust input data. and see the result

Objective

You have the model.
You set goal the result and try to set input.
finally. you have a plan follow the goal with you custom input(like a playing game)
(optional)it shoud be automatic & have multi plan.


## The flow step is:
part 1:
- multi input data. from csv
- train the model with data
- predict & tunning
- save model
- call model

part 2:
- adjust input
- see the result

part 3:
- set the goal result
- generate plan

---

## Pre-Develop
### generate virtual environments
```python
python3 -m venv .venv
```
### active virtual environment
```sh
source .venv/bin/activate
```
### deactive
```sh
deactivate
```

### install
```python
pip install -r requirements.txt
```

## Run

### Prepare Data
generate data to "data.csv" file.
```shell
python gen_data.py > data.csv
```

### Trainning
trainning and testing

```
python main.py > data.csv
```
