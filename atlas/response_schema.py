"""Versioned provider-enforced JSON condition, separate from historical text runs."""
PROTOCOL_ID = 'great-circle-json-object-v3'
PARSER_ID = 'json_distance_v3'
SCHEMA = {
    'type': 'object',
    'properties': {'distance_km': {'type': 'number', 'description': 'Estimated great-circle distance in kilometres.'}},
    'required': ['distance_km'],
    'additionalProperties': False,
}
# No geographic bounds in the output schema: response structure must not supply
# an answer constraint. Numerical plausibility is assessed separately by QC.
PROMPTS = {
    'en': 'Estimate the straight-line great-circle distance in kilometres between {city_a}, {country_a} and {city_b}, {country_b}. Return a JSON object with a single numeric field named "distance_km" containing your best estimate. Do not explain your reasoning.',
    'fr': 'Estimez la distance à vol d’oiseau, suivant un grand cercle, en kilomètres entre {city_a}, {country_a} et {city_b}, {country_b}. Répondez par un objet JSON contenant un seul champ numérique nommé "distance_km" avec votre meilleure estimation. N’expliquez pas votre raisonnement.',
    'es': 'Estima la distancia de círculo máximo, es decir, la distancia más corta sobre la superficie terrestre, en kilómetros entre {city_a}, {country_a} y {city_b}, {country_b}. Devuelve un objeto JSON con un único campo numérico llamado "distance_km" que contenga tu mejor estimación. No expliques tu razonamiento.',
    'ar': 'قدّر أقصر مسافة على سطح الأرض على طول دائرة عظمى، بالكيلومترات، بين {city_a}، {country_a} و{city_b}، {country_b}. أعد كائن JSON يحتوي على حقل عددي واحد باسم "distance_km" يتضمن أفضل تقدير لديك. لا تشرح طريقة استدلالك.',
    'zh': '请估计{city_a}（{country_a}）与{city_b}（{country_b}）之间的大圆距离，即沿地球表面的最短距离，单位为千米。返回一个JSON对象，其中只包含一个名为"distance_km"的数值字段，填入你认为最准确的估计。不要解释推理过程。',
}
