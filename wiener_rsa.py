import sympy
import RSAvulnerableKeyGenerator
import binascii

def hack_RSA(e, n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = sympy.continued_fraction_rational(e, n)
    convergents = sympy.convergents(frac)

    for (k, d) in convergents:

        # check if d is actually the key
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s * s - 4 * n
            if discr >= 0:
                t = sympy.sqrt(discr)
                if t.is_integer and (s + t) % 2 == 0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5

    while times > 0:
        e, n, d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)

        hacked_d = hack_RSA(e, n)

        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")

        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1

if __name__ == "__main__":
    e = 5888509129483318733141015540684847561532089231660075201362475202052296359580843241369355360704011646822761311787991096851475973157231557254766780057572768428628821260266097843818073736166414522085005139114354488263451168354466764469559633351657393916921023726636704060354584481520736047319632736089081616483
    n = 69220692452978837611584722489251562815563515968622649364574493397916874768751289888344631125027319952704576216989131429458589464882379411517016057847623832411538674466755326359437493887128746872377862465859891147261687428835985929008088250827938687801987323150396529439827662432314519477115478857456699371283
    c = 65733928466500769463675386952578429587241210775171226409262036946242160531524121603702893292951189436939807069576292554964867260712083342563197075560143585692779810092725435653941667836925416444042271853314655613726291165046934468052443555036125158738361053494262690595813597201022626206661383934415988054017
    d = hack_RSA(e, n)
    p = pow(c, d, n)
    st = "{:x}".format(p)
    print(st)
    print(binascii.unhexlify(st))


    

    