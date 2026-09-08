import numpy as np
import pytest

from atlas.inference import holm, permutation_comparison


def test_identical_constant_answers_cannot_support_difference():
    a = np.tile(np.arange(1, 31)[:, None]*100, (1, 10))
    result = permutation_comparison(a, a, a[:, 0], permutations=99)
    assert result['judgment_p'] == result['accuracy_p'] == 1
    assert result['mean_absolute_median_disagreement_km'] == 0


def test_separated_answers_have_detectable_effect_and_correct_sign():
    a = np.tile(np.arange(1, 31)[:, None]*100, (1, 10))
    result = permutation_comparison(a, a+100, a[:, 0], permutations=99)
    assert result['judgment_p'] == result['accuracy_p'] == .01
    assert result['mae_difference_b_minus_a_km'] == 100
    # Batch boundaries do not affect seed-controlled permutations.
    assert result == permutation_comparison(a, a+100, a[:, 0], permutations=99, batch=7)


def test_holm_and_shape_guards():
    assert np.allclose(holm([.01, .04, .03]), [.03, .06, .06])
    with pytest.raises(ValueError):
        holm([float('nan')])
    with pytest.raises(ValueError):
        permutation_comparison(np.ones((3, 10)), np.ones((2, 10)), np.ones(3))
