name: "反馈Bug / Bug Report"
description: 在这里反馈你遇到的Bug / Here to submit you founded bug
title: "📄[Bug Report] 请输入标题 / Please enter the title"
labels: ["bug"]
body:
    - type: checkboxes
      id: check-list
      attributes:
          label: "检查项 / Checks"
          description: "请逐个检查下列项目，并勾选确认。 / Please read these checks, and confirm."
          options:
              - label: "我确认有此Bug并知道如何复现 / I confirm that this bug exists and know how to reproduce it"
                required: true
              - label: "我确认有此Bug但不知如何复现 / I confirm that this bug exists but I don't know how to reproduce it"
                required: true
    - type: textarea
      id: description
      attributes:
          label: "描述问题 / Problem Description"
          description: 请简单描述您遇到的问题 / Please briefly describe the problem you encountered
          placeholder: 问题描述 / Problem Description
          render: bash
      validations:
          required: true
    - type: textarea
      id: reprod
      attributes:
          label: "如何复现你的遇到的问题？ / How do you reproduce the problem you encounter?"
          description: 请详细描述如何复现你遇到的问题 / Please describe in detail how to reproduce the problem you encountered
          value: |
              1. 
              2. 
              3. 
              4. 
              5. 问题复现 / Problem reproduction
          render: bash
      validations:
          required: true
    - type: textarea
      id: screenshots
      attributes:
          label: 截图 / screenshots
          description: 如果有相关截图的话，请上传截图。 / If you have relevant screenshots, please upload them.
          placeholder: 请把截图粘贴到这里
    - type: dropdown
      id: dropdown
