import random
import string

def generate_otp(length=6):
    """Simple OTP generator for testing"""
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))

def test_generate_otp_length():
    otp = generate_otp()
    assert len(otp) == 6

def test_generate_otp_is_digits():
    otp = generate_otp()
    assert otp.isdigit()

def test_generate_otp_uniqueness():
    otp1 = generate_otp()
    otp2 = generate_otp()
    assert otp1 != otp2  # OTPs should not be the same most of the time
