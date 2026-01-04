# 📂 Django Projects – Different View Approaches

This repository contains **3 Django projects** with the same overall structure and functionality.  
The key difference lies in how the **views** are implemented:

## 📁 Project Structure
Each project follows the same organization:
- `manage.py`
- Main app with `models.py`, `views.py`, `urls.py`
- Templates and configuration in `settings.py`

## 🔑 Differences Between Projects
- **1_function_based_view**  
  👉 Uses **Function-Based Views (FBVs)**.  
  Views are simple Python functions that take a request and return a response.

- **2_class_based_view**  
  👉 Uses **Class-Based Views (CBVs)**.  
  Views are classes that inherit from `View` or other Django base classes, offering better organization and reusability.

- **3_generic_class_based_view**  
  👉 Uses **Generic Class-Based Views (GCBVs)**.  
  Leverages Django’s built-in generic views like `ListView`, `DetailView`, `CreateView`, etc., reducing boilerplate code.

## 🎯 Purpose
The goal of this repository is to demonstrate how the **same application** can be built using different approaches in Django, allowing you to compare:
- 📝 Simplicity vs. Flexibility  
- 🔄 Code Reuse  
- 🛠️ Maintainability and Clarity  

## 🚀 How to Run
1. Navigate to the desired project folder:
   ```bash
   cd 1_function_based_view
