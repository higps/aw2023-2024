def any_arrows(arrows):
    for arrow in arrows:

        damaged = arrow.get('damaged', False)
        if not damaged:
            print("Not damaged arrow", arrow)
            pass
       # else:
           # print("Damaged arrow on ", arrow)
    
    return False

        
    

#You have a quiver of arrows, but some have been damaged. The quiver contains arrows with an optional range information 
# (different types of targets are positioned at different ranges), so each item is an arrow.
#You need to verify that you have some good ones left, in order to prepare for battle:
# If an arrow in the quiver does not have a damaged status, it means it's new.
# The expected result is a boolean, indicating whether you have any good arrows left.
any_arrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}])

# any_arrows([])
# any_arrows([{'range': 5, 'damaged': False}])
# any_arrows([{'range': 5, 'damaged': False},{'range': 15, 'damaged': True}])
# any_arrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}])
# any_arrows([{'range': 10, 'damaged': True}, {'damaged': True}])