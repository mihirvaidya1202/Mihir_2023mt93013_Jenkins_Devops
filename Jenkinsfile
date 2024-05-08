pipeline:
  agent: any
  
  stages:
    - stage: Checkout
      steps:
        - checkout: git://github.com/mihirvaidya1202/Mihir_2023mt93013_Jenkins_Devops
    
    - stage: Build
      steps:
        - sh: python setup.py build

    - stage: Execute Python Script
      steps:
        - sh: python test.py