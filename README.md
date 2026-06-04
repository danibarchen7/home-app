# 🏠 AI-Powered Peer-to-Peer Hospitality & Real Estate Marketplace (Syria)

A localized, full-stack cross-platform mobile application tailored for the Syrian peer-to-peer property listing and rental market. Built with a modular **Flutter** mobile client and a robust **Django** REST API, this platform integrates custom deep learning models directly into its architecture to automatically moderate community feedback and verify property imagery upon upload.

### 🔗 [Live Demo Link] | 🔗 [Graduation Project Presentation / Video Walkthrough]

---

## 📌 Overview
This application serves as a localized alternative to global accommodation platforms, optimized for the unique dynamics of the Syrian housing and rental market. Beyond standard property search, booking mechanics, and listing management, the platform solves core content-moderation and quality-assurance challenges autonomously using integrated artificial intelligence. 

By leveraging **Deep Learning**, the platform automates two crucial operational bottlenecks:
1. **Visual Quality Control:** Instantly analyzing uploaded user media to verify if it is an authentic property structure (House/Apartment) versus an invalid image.
2. **Community Trust & Safety:** Processing user reviews through a text-classification pipeline to filter, flag, or categorize feedback automatically.

## 🧠 Integrated AI & Deep Learning Pipelines

### 📸 1. Computer Vision: Property Image Classifier
* **Objective:** Automatically audit property imagery upon user upload to prevent fraudulent or irrelevant listings.
* **Architecture:** Custom Deep Convolutional Neural Network (CNN) trained with TensorFlow/Keras.
* **Functionality:** Classifies incoming uploads into `House`, `Apartment`, or `Invalid/Not a Property`. If flagged as invalid, the Flutter frontend intercepts the warning and prevents the invalid image from corrupting marketplace search results.

### 💬 2. NLP: Text & Comment Classification Engine
* **Objective:** Streamline review moderation and analyze sentiment dynamics within community feedback.
* **Architecture:** Text classification engine utilizing NLP preprocessing pipelines.
* **Functionality:** Scans and classifies text payloads from user reviews to assess sentiment parity or automatically flag toxic/spam language before it updates on the global database feed.

---

## ⚙️ Backend & Architecture Features (Django)
* **Custom User Model Extensibility:** Overrode Django's default `User` model to implement an optimized authentication flow suited for distinct roles (Hosts vs. Guests), managing custom profiles and regional data natively.
* **RESTful API Architecture:** Exposes secure endpoints handling complex queries, property listings, and nested serialized data for the Flutter client.
* **Admin Dashboard Control:** Leveraging Django's native admin panel, allowing administrators to audit flagged listings, manage user accounts, and update system parameters effortlessly.

## 📱 Mobile Client Features (Flutter)
* **Cross-Platform Performance:** Single-codebase native mobile application delivering high performance on iOS and Android.
* **State Management & UI Dynamics:** Built with clean asynchronous state handling to seamlessly manage photo uploads, dynamic menu maps, and real-time calculation overlays.
* **Optimized Image Uploads:** Image compression and processing logic before pushing multi-part imagery payloads to the Django backend.

---

## 🛠️ Tech Stack & Architecture Diagram

```text
[ Flutter Mobile Client ] ──(REST API Requests)──> [ Django Backend API ]
         ▲                                                │
         │                                      (Custom User Model Auth)
         │                                                │
 (Renders UI State) <──(JSON Response + Inference) ◄─────┴───► [ Deep Learning Models ]
                                                               (TensorFlow/Inference Engines)
