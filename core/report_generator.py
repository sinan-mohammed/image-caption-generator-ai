def generate_report(results, idea):
    report = f"""
# AI SaaS Validation Report

## Executive Summary
Startup Idea: {idea}

---

## Market Analysis
{results['market']}

---

## Competitor Landscape
{results['competitors']}

---

## Monetization Strategy
{results['monetization']}

---

## Risk Assessment
{results['risks']}
"""
    return report