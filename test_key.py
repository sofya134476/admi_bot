import os
import requests

# ===== ВСТАВЬ СВОЙ КЛЮЧ СЮДА ПРЯМО В КОД =====
OPENROUTER_KEY = "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"  # <--- ВСТАВЬ СВОЙ НОВЫЙ КЛЮЧ!
# ============================================

def test_openrouter():
    print("🔍 Тестируем OpenRouter...")
    print(f"🔑 Ключ: {OPENROUTER_KEY[:15]}...")
    
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openrouter/aurora-alpha",
                "messages": [
                    {"role": "user", "content": "Привет! Напиши 'Тест успешен'"}
                ]
            },
            timeout=10
        )
        
        print(f"📡 Статус ответа: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ УСПЕХ! Ответ OpenRouter:")
            print(result["choices"][0]["message"]["content"])
        else:
            print("❌ Ошибка!")
            print(response.text)
            
    except Exception as e:
        print(f"❌ Исключение: {e}")

if __name__ == "__main__":
    test_openrouter()