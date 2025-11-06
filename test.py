import pytest

from testbook import testbook
import numpy as np

def test_diffusion():
    with testbook('2_oop.ipynb', execute=True) as tb:
        Diffusion = tb.ref("Diffusion")

        try:
            model = Diffusion(L=5,dx=0.2,dt=0.0001)
            model.set_pde_params(kappa=2)
            model.set_bcs(init=20,left=50,right=10)
            model.solve(n_steps=1000)
        except Exception as excinfo:
            pytest.fail(f"Unexpected exception raised: {excinfo}")


        assert np.isclose(model.T[0,0], 20.0), 'Diffusion class: Wrong temperature field at t=0'
        assert np.isclose(model.T[1,0], 50.0), 'Diffusion class: Wrong BC on the left boundary'
        assert np.isclose(model.T[100,-1], 21.349927649838786), 'Diffusion class: Wrong BC on the right boundary or wrong solution in the interior of the domain'
        assert np.isclose(model.T[999,5],  23.475072280558898), 'Diffusion class: Wrong BC on the right boundary or wrong solution in the interior of the domain'

def test_mydiffusion():
    with testbook('2_oop.ipynb', execute=True) as tb:
        MyDiffusion = tb.ref("MyDiffusion")

        try:
            new_model = MyDiffusion(L=10,dx=0.1,dt=0.0001)
            new_model.set_pde_params(kappa=10)
            new_model.set_bcs(init=250,left=10,right=500)
            new_model.solve(n_steps=1000)
        except Exception as excinfo:
            pytest.fail(f"Unexpected exception raised: {excinfo}")

        assert np.isclose(new_model.T[0,0], 250.0), 'MyDiffusion class: Wrong temperature field at t=0'
        assert np.isclose(new_model.T[1,0], 10.0), 'MyDiffusion class: Wrong BC on the left boundary'
        assert np.isclose(new_model.T[100,-1], 500.0), 'MyDiffusion class: Wrong BC on the right boundary'
        assert np.isclose(new_model.T[999,5], 76.37073760308783), 'MyDiffusion class: Wrong solution in the interior of the domain' 

