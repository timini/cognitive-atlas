"""Versioned translations: instruction language varies; canonical entity names stay fixed."""
LANGUAGE_LABELS = {'en': 'English', 'fr': 'French', 'es': 'Spanish', 'ar': 'Arabic', 'zh': 'Mandarin Chinese'}
PROTOCOL_ID = 'great-circle-formatted-number-v2'
PARSER_ID = 'ascii_decimal_v2'
PROMPTS = {
    'en': 'Estimate the straight-line great-circle distance in kilometres between {city_a}, {country_a} and {city_b}, {country_b}. Return only your best numerical estimate in kilometres. Do not explain your reasoning. Use only digits 0–9, with a period if a decimal separator is needed. Do not include thousands separators or units.',
    'fr': 'Estimez la distance à vol d’oiseau, suivant un grand cercle, en kilomètres entre {city_a}, {country_a} et {city_b}, {country_b}. Répondez uniquement par votre meilleure estimation numérique en kilomètres, sans expliquer votre raisonnement. Utilisez uniquement les chiffres 0–9, avec un point si un séparateur décimal est nécessaire. N’incluez ni séparateur de milliers ni unité.',
    'es': 'Estima la distancia de círculo máximo, es decir, la distancia más corta sobre la superficie terrestre, en kilómetros entre {city_a}, {country_a} y {city_b}, {country_b}. Devuelve únicamente tu mejor estimación numérica en kilómetros. No expliques tu razonamiento. Utiliza solo los dígitos 0–9, con un punto si necesitas un separador decimal. No incluyas separadores de miles ni unidades.',
    'ar': 'قدّر أقصر مسافة على سطح الأرض على طول دائرة عظمى، بالكيلومترات، بين {city_a}، {country_a} و{city_b}، {country_b}. أعد أفضل تقدير عددي فقط بالكيلومترات. لا تشرح طريقة استدلالك. استخدم الأرقام 0–9 فقط، مع نقطة إذا احتجت إلى فاصل عشري. لا تُضمّن فواصل الآلاف أو وحدات القياس.',
    'zh': '请估计{city_a}（{country_a}）与{city_b}（{country_b}）之间的大圆距离，即沿地球表面的最短距离，单位为千米。只返回你认为最准确的千米数值估计，不要解释推理过程。仅使用数字0–9，如需小数分隔符，请使用英文句点。不要包含千位分隔符或单位。',
}
ENTITY_NAME_POLICY = 'canonical_English_city_and_country_names_unchanged'
TRANSLATION_REVIEW = 'Assistant-authored translations; no independent native-speaker validation claimed'
